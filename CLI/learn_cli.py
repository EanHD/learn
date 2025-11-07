#!/usr/bin/env python3
"""
Enhanced Learn CLI - Full-Featured Interactive Learning System with Rich Output
"""

import os
import sys
import json
import subprocess
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import argparse

# Rich for beautiful terminal output
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.syntax import Syntax
    from rich.markdown import Markdown
    from rich.layout import Layout
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("[!!] Rich library not available. Install with: pip install rich")

# Import new modules for modernization
try:
    from CLI import languages
    from CLI import utils
    from CLI import config as cfg_module
except ImportError:
    # Fallback for development
    try:
        import languages
        import utils
        import config as cfg_module
    except ImportError:
        print("Warning: Could not import modernization modules")
        languages = None
        utils = None
        cfg_module = None

# Create global console for rich output
console = Console() if RICH_AVAILABLE else None


class SystemChecker:
    """Checks system dependencies and provides fix commands"""

    def __init__(self):
        self.checks = []
        if utils:
            self.os_type = utils.get_platform()
        else:
            self.os_type = self._detect_os()
    
    def _detect_os(self) -> str:
        """Detect operating system (fallback)"""
        if sys.platform == "win32":
            return "windows"
        elif sys.platform == "darwin":
            return "mac"
        else:
            return "linux"

    def check_all(self) -> bool:
        """Run all checks and return True if all pass"""
        self.checks = []

        # Check Neovim
        nvim_ok = self._check_command("nvim", "--version")
        self.checks.append({
            "name": "Neovim",
            "status": "OK" if nvim_ok else "MISSING",
            "fix": self._get_install_command("neovim") if not nvim_ok else None,
            "version": self._get_nvim_version() if nvim_ok else None
        })

        # Check compilers
        gcc_ok = self._check_command("gcc", "--version")
        self.checks.append({
            "name": "GCC (C/C++ compiler)",
            "status": "OK" if gcc_ok else "MISSING",
            "fix": self._get_install_command("gcc") if not gcc_ok else None
        })

        clangd_ok = self._check_command("clangd", "--version")
        self.checks.append({
            "name": "clangd (C++ LSP)",
            "status": "OK" if clangd_ok else "MISSING",
            "fix": self._get_install_command("clangd") if not clangd_ok else None
        })

        # Check Rust
        rustc_ok = self._check_command("rustc", "--version")
        self.checks.append({
            "name": "Rust compiler",
            "status": "OK" if rustc_ok else "MISSING",
            "fix": self._get_install_command("rust") if not rustc_ok else None
        })

        # Check Node
        node_ok = self._check_command("node", "--version")
        self.checks.append({
            "name": "Node.js",
            "status": "OK" if node_ok else "MISSING",
            "fix": self._get_install_command("node") if not node_ok else None,
            "version": self._get_command_output("node", "--version") if node_ok else None
        })

        # Check Python
        python_cmd = "python" if self.os_type == "windows" else "python3"
        python_ok = self._check_command(python_cmd, "--version")
        self.checks.append({
            "name": "Python 3",
            "status": "OK" if python_ok else "MISSING",
            "fix": self._get_install_command("python") if not python_ok else None
        })

        # Check Mason packages
        mason_ok = self._check_mason_packages()
        self.checks.append({
            "name": "Mason LSP packages",
            "status": "OK" if mason_ok else "INCOMPLETE",
            "fix": "nvim --headless '+MasonInstall clangd rust-analyzer pyright ts_ls' +qa" if not mason_ok else None,
            "details": self._get_mason_status()
        })

        # Check Kickstart
        if self.os_type == "windows":
            kickstart_ok = Path.home() / "AppData" / "Local" / "nvim" / "init.lua"
        else:
            kickstart_ok = Path.home() / ".config" / "nvim" / "init.lua"
        
        self.checks.append({
            "name": "Kickstart.nvim config",
            "status": "OK" if kickstart_ok.exists() else "MISSING",
            "fix": self._get_nvim_config_command() if not kickstart_ok.exists() else None
        })

        return all(c["status"] == "OK" for c in self.checks if c["name"] not in ["Mason LSP packages", "Kickstart.nvim config"])

    def _check_command(self, cmd: str, *args) -> bool:
        """Check if a command exists and runs"""
        try:
            subprocess.run([cmd, *args], capture_output=True, check=False, timeout=2)
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def _get_command_output(self, cmd: str, *args) -> Optional[str]:
        """Get command output"""
        try:
            result = subprocess.run([cmd, *args], capture_output=True, text=True, timeout=2)
            return result.stdout.strip().split('\n')[0]
        except:
            return None

    def _get_nvim_version(self) -> Optional[str]:
        """Get Neovim version"""
        try:
            result = subprocess.run(["nvim", "--version"], capture_output=True, text=True)
            first_line = result.stdout.split('\n')[0]
            return first_line.replace("NVIM ", "")
        except:
            return None

    def _get_mason_dir(self) -> Path:
        """Get Mason packages directory (cross-platform)"""
        if self.os_type == "windows":
            return Path.home() / "AppData" / "Local" / "nvim-data" / "mason" / "packages"
        else:
            return Path.home() / ".local" / "share" / "nvim" / "mason" / "packages"
    
    def _check_mason_packages(self) -> bool:
        """Check if Mason packages are installed"""
        mason_dir = self._get_mason_dir()
        if not mason_dir.exists():
            return False

        required = {"clangd", "rust-analyzer", "pyright", "prettierd", "stylua"}
        installed = {p.name for p in mason_dir.iterdir() if p.is_dir()}
        return required.issubset(installed)

    def _get_mason_status(self) -> str:
        """Get Mason package status"""
        mason_dir = self._get_mason_dir()
        if not mason_dir.exists():
            return "Mason directory not found"

        installed = sorted([p.name for p in mason_dir.iterdir() if p.is_dir()])
        return f"{len(installed)} packages installed"
    
    def _get_install_command(self, package: str) -> str:
        """Get OS-specific installation command"""
        commands = {
            "neovim": {
                "linux": "sudo apt install neovim  # or: sudo dnf install neovim",
                "mac": "brew install neovim",
                "windows": "choco install neovim  # or: scoop install neovim"
            },
            "gcc": {
                "linux": "sudo apt install build-essential",
                "mac": "xcode-select --install  # or: brew install gcc",
                "windows": "choco install mingw  # or download from https://www.mingw-w64.org/"
            },
            "clangd": {
                "linux": "sudo apt install clangd",
                "mac": "brew install llvm",
                "windows": "choco install llvm"
            },
            "rust": {
                "linux": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
                "mac": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
                "windows": "Download from https://rustup.rs/ and run installer"
            },
            "node": {
                "linux": "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs",
                "mac": "brew install node",
                "windows": "choco install nodejs  # or download from https://nodejs.org/"
            },
            "python": {
                "linux": "sudo apt install python3",
                "mac": "brew install python3",
                "windows": "choco install python  # or download from https://www.python.org/"
            }
        }
        return commands.get(package, {}).get(self.os_type, f"Install {package} for {self.os_type}")
    
    def _get_nvim_config_command(self) -> str:
        """Get OS-specific Neovim config installation command"""
        if self.os_type == "windows":
            return "git clone https://github.com/nvim-lua/kickstart.nvim.git $env:LOCALAPPDATA\\nvim"
        else:
            return "git clone https://github.com/nvim-lua/kickstart.nvim.git ~/.config/nvim"

    # Language runtime checks
    LANGUAGE_RUNTIMES = {
        "c-c++": {
            "cmd": "gcc",
            "name": "GCC/G++",
            "install": {
                "linux": "sudo apt install build-essential",
                "mac": "xcode-select --install",
                "windows": "choco install mingw"
            }
        },
        "rust": {
            "cmd": "rustc",
            "name": "Rust compiler",
            "install": {
                "linux": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
                "mac": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
                "windows": "Download from https://rustup.rs/"
            }
        },
        "python": {
            "cmd": {"linux": "python3", "mac": "python3", "windows": "python"},
            "name": "Python 3",
            "install": {
                "linux": "sudo apt install python3",
                "mac": "brew install python3",
                "windows": "choco install python"
            }
        },
        "javascript": {
            "cmd": "node",
            "name": "Node.js",
            "install": {
                "linux": "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs",
                "mac": "brew install node",
                "windows": "choco install nodejs"
            }
        },
        "typescript": {
            "cmd": "node",
            "name": "Node.js",
            "install": {
                "linux": "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs",
                "mac": "brew install node",
                "windows": "choco install nodejs"
            }
        },
        "go": {
            "cmd": "go",
            "name": "Go compiler",
            "install": {
                "linux": "sudo apt install golang-go",
                "mac": "brew install go",
                "windows": "choco install golang"
            }
        },
        "lua": {
            "cmd": "lua",
            "name": "Lua interpreter",
            "install": {
                "linux": "sudo apt install lua5.4",
                "mac": "brew install lua",
                "windows": "choco install lua"
            }
        },
        "dart": {
            "cmd": "dart",
            "name": "Dart SDK",
            "install": {
                "linux": "sudo apt install dart",
                "mac": "brew install dart",
                "windows": "choco install dart-sdk"
            }
        },
        "swift": {
            "cmd": "swift",
            "name": "Swift compiler",
            "install": {
                "linux": "sudo apt install swift",
                "mac": "Already installed with Xcode",
                "windows": "Download from https://swift.org/download/"
            }
        },
        "kotlin": {
            "cmd": "kotlinc",
            "name": "Kotlin compiler",
            "install": {
                "linux": "sudo apt install kotlin",
                "mac": "brew install kotlin",
                "windows": "choco install kotlinc"
            }
        },
        "java": {
            "cmd": "javac",
            "name": "Java compiler",
            "install": {
                "linux": "sudo apt install default-jdk",
                "mac": "brew install openjdk",
                "windows": "choco install openjdk"
            }
        },
        "csharp": {
            "cmd": {"linux": "csc", "mac": "csc", "windows": "csc"},
            "name": "C# compiler (.NET)",
            "install": {
                "linux": "sudo apt install dotnet-sdk-latest",
                "mac": "brew install dotnet",
                "windows": "choco install dotnet-sdk"
            }
        },
        "shell": {
            "cmd": "bash",
            "name": "Bash shell",
            "install": {
                "linux": "Already installed",
                "mac": "Already installed",
                "windows": "Git Bash (comes with Git) or WSL"
            }
        },
        "powershell": {
            "cmd": "pwsh",
            "name": "PowerShell Core",
            "install": {
                "linux": "sudo apt install -y powershell",
                "mac": "brew install powershell",
                "windows": "Already installed (or choco install powershell-core)"
            }
        },
        "zig": {
            "cmd": "zig",
            "name": "Zig compiler",
            "install": {
                "linux": "Download from https://ziglang.org/download/",
                "mac": "brew install zig",
                "windows": "choco install zig"
            }
        },
        "sql": {
            "cmd": "sqlite3",
            "name": "SQLite3",
            "install": {
                "linux": "sudo apt install sqlite3",
                "mac": "brew install sqlite3",
                "windows": "choco install sqlite"
            }
        },
        "julia": {
            "cmd": "julia",
            "name": "Julia language",
            "install": {
                "linux": "Download from https://julialang.org/downloads/",
                "mac": "brew install julia",
                "windows": "choco install julia"
            }
        },
        "r": {
            "cmd": "R",
            "name": "R language",
            "install": {
                "linux": "sudo apt install r-base",
                "mac": "brew install r",
                "windows": "choco install r.project"
            }
        },
        "php": {
            "cmd": "php",
            "name": "PHP interpreter",
            "install": {
                "linux": "sudo apt install php-cli",
                "mac": "brew install php",
                "windows": "choco install php"
            }
        },
        "nosql": {
            "cmd": "mongosh",
            "name": "MongoDB shell",
            "install": {
                "linux": "Visit https://www.mongodb.com/try/download/shell",
                "mac": "brew install mongosh",
                "windows": "choco install mongodb-shell"
            }
        },
    }

    def check_language_runtime(self, language: str) -> Tuple[bool, str, Optional[str]]:
        """Check if a language runtime is available

        Returns: (is_available, display_name, install_command)
        """
        if language not in self.LANGUAGE_RUNTIMES:
            return True, language, None  # Unknown language, assume available

        runtime_info = self.LANGUAGE_RUNTIMES[language]
        
        # Get command (may be OS-specific)
        cmd = runtime_info["cmd"]
        if isinstance(cmd, dict):
            cmd = cmd.get(self.os_type, cmd.get("linux", ""))
        
        name = runtime_info["name"]
        
        # Get install command for current OS
        install = runtime_info["install"]
        if isinstance(install, dict):
            install = install.get(self.os_type, install.get("linux", ""))

        is_available = self._check_command(cmd, "--version")
        return is_available, name, install if not is_available else None

    def check_multiple_languages(self, languages: List[str]) -> Dict[str, Dict]:
        """Check runtimes for multiple languages

        Returns: {language: {available, name, install_cmd}}
        """
        results = {}
        for language in languages:
            available, name, install_cmd = self.check_language_runtime(language)
            results[language] = {
                "available": available,
                "name": name,
                "install_cmd": install_cmd
            }
        return results

    def print_report(self):
        """Print formatted check report using Rich"""
        if console:
            # Create a rich table
            table = Table(title="◽ SYSTEM CHECK", show_header=True, header_style="bold cyan")
            table.add_column("Component", style="cyan")
            table.add_column("Status", style="green")
            table.add_column("Details", style="dim white")

            for check in self.checks:
                status = "[bold green][OK][/bold green]" if check["status"] == "OK" else "[bold yellow][!!][/bold yellow]"
                details = ""

                if check.get("version"):
                    details = f"v{check['version']}"
                elif check.get("details"):
                    details = check["details"]

                table.add_row(check["name"], status, details)

            console.print(table)

            # Show fixes if needed
            fixes_needed = [c for c in self.checks if c["status"] != "OK" and c.get("fix")]
            if fixes_needed:
                console.print("\n[bold yellow]◽ MISSING COMPONENTS[/bold yellow]")
                for check in fixes_needed:
                    console.print(f"  [dim]{check['name']}:[/dim]")
                    console.print(f"    [cyan]{check['fix']}[/cyan]")
        else:
            # Fallback to plain text
            print("\n" + "=" * 70)
            print("  SYSTEM CHECK REPORT")
            print("=" * 70 + "\n")

            for check in self.checks:
                status_icon = "[OK]" if check["status"] == "OK" else "[!!]"
                print(f"{status_icon} {check['name']}")

                if check.get("version"):
                    print(f"    Version: {check['version']}")

                if check.get("details"):
                    print(f"    Status: {check['details']}")

                if check["status"] != "OK" and check.get("fix"):
                    print(f"    Fix: {check['fix']}")

                print()


class InitWizard:
    """First-run setup wizard"""

    def __init__(self, learn_dir: Path):
        self.learn_dir = learn_dir
        self.checker = SystemChecker()
        # Use cross-platform workspace location
        if utils:
            if self.checker.os_type == "windows":
                self.workspace_root = Path.home() / "AppData" / "Local" / "learn" / "workspaces"
            elif self.checker.os_type == "mac":
                self.workspace_root = Path.home() / "Library" / "Application Support" / "learn" / "workspaces"
            else:
                self.workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"
        else:
            self.workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"

    def run(self):
        """Run the initialization wizard"""
        self._clear_screen()
        if console:
            console.print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
            console.print("[bold cyan]◽ LEARN CLI[/bold cyan]")
            console.print("[bold cyan]   FIRST-TIME SETUP[/bold cyan]")
            console.print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
            console.print("\n[bold]This wizard will:[/bold]")
            console.print("  [cyan]1[/cyan]  Check your system dependencies")
            console.print("  [cyan]2[/cyan]  Install missing components")
            console.print("  [cyan]3[/cyan]  Set up your learning workspace")
            console.print("  [cyan]4[/cyan]  Configure your preferred editor")
            console.print("\n[dim]Estimated time: 5 minutes[/dim]\n")
        else:
            print("=" * 70)
            print("  LEARN CLI - FIRST-TIME SETUP WIZARD")
            print("=" * 70)
            print("\nThis wizard will:")
            print("  1. Check your system dependencies")
            print("  2. Install missing components")
            print("  3. Set up your learning workspace")
            print("  4. Configure your preferred editor")
            print("\nEstimated time: 5 minutes\n")

        input("Press Enter to begin...")

        # Step 1: System check
        self._step_system_check()

        # Step 2: Editor selection
        self._step_editor_selection()

        # Step 3: Workspace setup
        self._step_workspace_setup()

        # Step 4: Completion
        self._step_completion()

    def _clear_screen(self):
        if utils:
            utils.clear_screen()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    def _step_system_check(self):
        """Check system dependencies"""
        self._clear_screen()
        print("=" * 70)
        print("  STEP 1: SYSTEM CHECK")
        print("=" * 70)

        print("\nChecking system dependencies...\n")
        all_ok = self.checker.check_all()
        self.checker.print_report()

        if not all_ok:
            print("Some dependencies are missing!")
            choice = input("\nWould you like to install them now? (y/N): ").strip().lower()

            if choice == 'y':
                self._install_missing_deps()
            else:
                print("\nYou can install them later and re-run: learn init")

        input("\nPress Enter to continue...")

    def _install_missing_deps(self):
        """Install missing dependencies"""
        print("\nInstalling missing dependencies...")
        
        os_type = self.checker.os_type
        if os_type == "linux":
            print("This may require sudo password.\n")
        elif os_type == "windows":
            print("Note: Some commands require Administrator privileges.\n")
        elif os_type == "mac":
            print("This may require your password.\n")

        for check in self.checker.checks:
            if check["status"] != "OK" and check.get("fix"):
                print(f"Installing {check['name']}...")
                print(f"  Command: {check['fix']}")

                confirm = input("  Run this command? (Y/n): ").strip().lower()
                if confirm != 'n':
                    if os_type == "windows" and "choco" in check['fix']:
                        # Check if running as admin on Windows
                        print("  Note: Chocolatey commands require Administrator privileges.")
                    os.system(check['fix'])

    def _step_editor_selection(self):
        """Select preferred editor"""
        self._clear_screen()
        if console:
            console.print(Panel.fit(
                "[bold cyan]STEP 2: EDITOR SELECTION[/bold cyan]",
                border_style="cyan"
            ))
            console.print("\n[bold]Choose your preferred editor mode:[/bold]\n")

            editors = [
                ("1", "Neovim (recommended)", [
                    "Split-screen with lesson + code",
                    "Full LSP support (autocomplete, diagnostics)",
                    "Auto-formatting on save"
                ]),
                ("2", "VS Code", [
                    "Opens lesson directory in VS Code",
                    "Use your existing VS Code setup",
                    "Graphical interface with Vim motions"
                ]),
                ("3", "Terminal (read-only)", [
                    "Simple markdown viewer",
                    "Use external editor for code",
                    "Distraction-free"
                ])
            ]

            for num, name, features in editors:
                console.print(f"  [cyan]{num}[/cyan]  [bold]{name}[/bold]")
                for feature in features:
                    console.print(f"     [dim]· {feature}[/dim]")
                console.print()
        else:
            print("=" * 70)
            print("  STEP 2: EDITOR SELECTION")
            print("=" * 70)
            print("\nChoose your preferred editor mode:\n")
            print("  1. Neovim (recommended)")
            print("     - Split-screen with lesson + code")
            print("     - Full LSP support (autocomplete, diagnostics)")
            print("     - Auto-formatting on save")
            print("")
            print("  2. VS Code")
            print("     - Opens lesson directory in VS Code")
            print("     - Use your existing VS Code setup")
            print("")
            print("  3. Terminal (read-only)")
            print("     - Simple markdown viewer")
            print("     - Use external editor for code")

        choice = input("\nSelect mode (1-3, default: 1): ").strip() or "1"

        mode_map = {"1": "vim", "2": "vscode", "3": "terminal"}
        selected_mode = mode_map.get(choice, "vim")

        config_file = self.learn_dir / ".learn-config.json"
        config = {"default_mode": selected_mode}
        config_file.write_text(json.dumps(config, indent=2))

        if console:
            console.print(f"\n[bold green][OK] Default mode set to: {selected_mode}[/bold green]")
        else:
            print(f"\nDefault mode set to: {selected_mode}")

        input("Press Enter to continue...")

    def _step_workspace_setup(self):
        """Set up learning workspace"""
        self._clear_screen()
        print("=" * 70)
        print("  STEP 3: WORKSPACE SETUP")
        print("=" * 70)

        print(f"\nCreating workspace directory at:")
        print(f"  {self.workspace_root}")

        self.workspace_root.mkdir(parents=True, exist_ok=True)

        # Create sample workspaces
        langs = ["cpp", "rust", "python", "javascript"]
        for lang in langs:
            lang_dir = self.workspace_root / lang
            lang_dir.mkdir(exist_ok=True)

        print("\nWorkspace created successfully!")
        print(f"\nYour code will be saved in: {self.workspace_root}")

        input("\nPress Enter to continue...")

    def _step_completion(self):
        """Completion message"""
        self._clear_screen()
        if console:
            console.print(Panel.fit(
                "[bold green]◽ SETUP COMPLETE[/bold green]",
                border_style="green"
            ))
            console.print("\n[bold]You're all set! Here's what to do next:[/bold]\n")
            console.print("  [cyan]1.[/cyan] Start your first lesson:")
            console.print("     [yellow]learn c++ 1[/yellow]")
            console.print("")
            console.print("  [cyan]2.[/cyan] Or browse all lessons:")
            console.print("     [yellow]learn --list[/yellow]")
            console.print("")
            console.print("  [cyan]3.[/cyan] Need help?")
            console.print("     [yellow]learn --help[/yellow]")
            console.print("")
            console.print("  [cyan]4.[/cyan] Check system anytime:")
            console.print("     [yellow]learn doctor[/yellow]")
            console.print("")
        else:
            print("=" * 70)
            print("  SETUP COMPLETE!")
            print("=" * 70)
            print("\nYou're all set! Here's what to do next:\n")
            print("  1. Start your first lesson:")
            print("     learn c++ 1")
            print("")
            print("  2. Or browse all lessons:")
            print("     learn --list")
            print("")
            print("  3. Need help?")
            print("     learn --help")
            print("")
            print("  4. Check system anytime:")
            print("     learn doctor")
            print("")

        input("Press Enter to return to main menu...")


class ProgressTracker:
    """Tracks user progress across all languages and lessons"""

    def __init__(self, learn_dir: Path):
        self.learn_dir = learn_dir
        self.progress_file = learn_dir / ".learn-progress.json"
        self.data = self._load_progress()

    def _load_progress(self) -> Dict:
        """Load progress data from JSON file"""
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._init_progress()
        return self._init_progress()

    def _init_progress(self) -> Dict:
        """Initialize empty progress structure"""
        return {
            "languages": {},
            "sessions": [],
            "started": datetime.now().isoformat(),
            "last_accessed": None
        }

    def _save_progress(self):
        """Save progress data to JSON file"""
        self.data["last_accessed"] = datetime.now().isoformat()
        with open(self.progress_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def mark_lesson_opened(self, language: str, stage: int, level: int, mode: str):
        """Mark a lesson as opened"""
        if language not in self.data["languages"]:
            self.data["languages"][language] = {}

        stage_key = f"stage_{stage}"
        if stage_key not in self.data["languages"][language]:
            self.data["languages"][language][stage_key] = {}

        level_key = f"level_{level}"
        if level_key not in self.data["languages"][language][stage_key]:
            self.data["languages"][language][stage_key][level_key] = {
                "opened_count": 0,
                "first_opened": datetime.now().isoformat(),
                "completed": False
            }

        self.data["languages"][language][stage_key][level_key]["opened_count"] += 1
        self.data["languages"][language][stage_key][level_key]["last_opened"] = datetime.now().isoformat()

        self.data["sessions"].append({
            "timestamp": datetime.now().isoformat(),
            "language": language,
            "stage": stage,
            "level": level,
            "mode": mode
        })

        self._save_progress()

    def mark_lesson_completed(self, language: str, stage: int, level: int):
        """Mark a lesson as completed"""
        stage_key = f"stage_{stage}"
        level_key = f"level_{level}"

        if (language in self.data["languages"] and
            stage_key in self.data["languages"][language] and
            level_key in self.data["languages"][language][stage_key]):

            self.data["languages"][language][stage_key][level_key]["completed"] = True
            self.data["languages"][language][stage_key][level_key]["completed_at"] = datetime.now().isoformat()
            self._save_progress()
            return True
        return False

    def get_language_progress(self, language: str) -> Dict:
        """Get progress for a specific language"""
        return self.data["languages"].get(language, {})

    def get_next_lesson(self, language: str) -> Optional[Tuple[int, int]]:
        """Suggest next lesson based on progress"""
        lang_progress = self.get_language_progress(language)

        if not lang_progress:
            return (1, 1)

        for stage in range(1, 6):
            stage_key = f"stage_{stage}"
            stage_progress = lang_progress.get(stage_key, {})

            for level in range(1, 8):
                level_key = f"level_{level}"
                level_data = stage_progress.get(level_key)

                if not level_data:
                    return (stage, level)

                if not level_data.get("completed", False):
                    return (stage, level)

        return None

    def get_completion_stats(self, language: str) -> Dict:
        """Get completion statistics for a language"""
        lang_progress = self.get_language_progress(language)
        total_lessons = 0
        completed_lessons = 0

        for stage in range(1, 6):
            stage_key = f"stage_{stage}"
            stage_progress = lang_progress.get(stage_key, {})

            for level in range(1, 8):
                level_key = f"level_{level}"
                total_lessons += 1
                level_data = stage_progress.get(level_key)

                if level_data and level_data.get("completed", False):
                    completed_lessons += 1

        return {
            "total": total_lessons,
            "completed": completed_lessons,
            "percentage": (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        }


class LessonManager:
    """Manages lesson discovery and operations"""

    def __init__(self, learn_dir: Path):
        self.learn_dir = learn_dir
        self.languages = self._discover_languages()

    def _discover_languages(self) -> Dict[str, str]:
        """Discover available languages dynamically"""
        lang_map = {}

        # Check all directories in the learn directory
        if self.learn_dir.exists():
            for item in self.learn_dir.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    # Check if this directory has stage subdirectories
                    stages = list(item.glob("stage-*"))
                    if stages:
                        lang_map[item.name] = item.name

        return lang_map

    def get_language_display_name(self, lang_code: str) -> str:
        """Get display name for language"""
        names = {
            "c-c++": "C++",
            "rust": "Rust",
            "python": "Python",
            "javascript": "JavaScript",
            "go": "Go",
            "lua": "Lua",
            "dart": "Dart",
            "swift": "Swift",
            "kotlin": "Kotlin",
            "sql": "SQL",
            "csharp": "C#",
            "shell": "Shell",
            "powershell": "PowerShell",
            "typescript": "TypeScript"
        }
        return names.get(lang_code, lang_code.title())

    def find_lesson(self, language: str, stage: int, level: int) -> Optional[Path]:
        """Find lesson path"""
        lang_path = self.learn_dir / language / f"stage-{stage}" / f"level-{level}" / "lesson.md"
        return lang_path if lang_path.exists() else None

    def list_all_lessons(self) -> Dict:
        """List all available lessons organized by language"""
        lessons = {}

        for lang_code, lang_name in self.languages.items():
            lang_path = self.learn_dir / lang_code
            lessons[lang_code] = {}

            for stage in range(1, 6):
                stage_path = lang_path / f"stage-{stage}"
                if not stage_path.exists():
                    continue

                lessons[lang_code][stage] = []

                for level in range(1, 8):
                    level_path = stage_path / f"level-{level}"
                    lesson_file = level_path / "lesson.md"

                    if lesson_file.exists():
                        lessons[lang_code][stage].append(level)

        return lessons

    def get_lesson_file_extension(self, language: str) -> str:
        """Get file extension for language"""
        extensions = {
            "c-c++": "cpp",
            "rust": "rs",
            "python": "py",
            "javascript": "js",
            "go": "go",
            "lua": "lua",
            "dart": "dart",
            "swift": "swift",
            "kotlin": "kt",
            "sql": "sql",
            "c#": "cs",
            "csharp": "cs",
            "shell": "sh",
            "powershell": "ps1",
            "typescript": "ts",
            "zig": "zig"
        }
        return extensions.get(language, "txt")


class LessonExecutor:
    """Executes lessons in different modes"""

    def __init__(self, lesson_manager: LessonManager):
        self.lesson_manager = lesson_manager
        self.workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"

    def open_vim(self, lesson_path: Path, language: str):
        """Open lesson in Vim mode with workspace scaffolding"""
        # Get lesson metadata
        level_dir = lesson_path.parent
        stage_num = level_dir.parent.name.replace("stage-", "")
        level_num = level_dir.name.replace("level-", "")

        # Create workspace for this lesson
        workspace = self._create_workspace(language, stage_num, level_num)

        # Show pre-launch instructions
        self._show_vim_instructions(workspace, language)

        # Get custom Lua init path (in MODE_VIM/CONFIG)
        lua_init_path = Path(__file__).parent.parent / "MODE_VIM" / "CONFIG" / "init-learning.lua"

        # Launch Neovim with our custom Lua config
        # Uses OneDark theme, lualine, and beautiful markdown rendering
        subprocess.run([
            "nvim",
            "-u", str(lua_init_path),  # Use our custom Lua config
            "-O",  # Vertical split
            str(lesson_path),  # Left: lesson (beautiful markdown)
            str(workspace["main_file"])  # Right: editable code
        ])

    def _create_workspace(self, language: str, stage: str, level: str) -> Dict:
        """Create workspace directory with starter files"""
        # Create workspace path
        lang_short = self._get_lang_short_name(language)
        workspace_dir = self.workspace_root / lang_short / f"stage-{stage}" / f"level-{level}"
        workspace_dir.mkdir(parents=True, exist_ok=True)

        # Helper function to check if file needs help comment
        def needs_help_comment(file_path: Path) -> bool:
            if not file_path.exists():
                return True
            content = file_path.read_text()
            # Check if file is empty or doesn't have help comment
            return len(content.strip()) == 0 or "Press" not in content or "Space" not in content or "help" not in content

        # Create starter files based on language
        if language == "c-c++":
            main_file = workspace_dir / "main.cpp"
            if needs_help_comment(main_file):
                self._create_cpp_workspace(workspace_dir)
        elif language == "rust":
            main_file = workspace_dir / "main.rs"
            if needs_help_comment(main_file):
                self._create_rust_workspace(workspace_dir)
        elif language == "python":
            main_file = workspace_dir / "main.py"
            if needs_help_comment(main_file):
                self._create_python_workspace(workspace_dir)
        elif language == "javascript":
            main_file = workspace_dir / "main.js"
            if needs_help_comment(main_file):
                self._create_js_workspace(workspace_dir)
        elif language == "zig":
            main_file = workspace_dir / "main.zig"
            if needs_help_comment(main_file):
                self._create_zig_workspace(workspace_dir)
        else:
            ext = self.lesson_manager.get_lesson_file_extension(language)
            main_file = workspace_dir / f"main.{ext}"
            if needs_help_comment(main_file):
                self._create_solution_template(main_file, language)

        return {
            "dir": workspace_dir,
            "main_file": main_file
        }

    def _get_lang_short_name(self, language: str) -> str:
        """Get short language name for workspace"""
        mapping = {
            "c-c++": "cpp",
            "rust": "rust",
            "python": "python",
            "javascript": "js",
            "go": "go",
            "lua": "lua",
            "dart": "dart",
            "swift": "swift",
            "kotlin": "kotlin",
            "sql": "sql",
            "c#": "csharp",
            "csharp": "csharp",
            "shell": "shell",
            "powershell": "powershell",
            "typescript": "typescript",
            "zig": "zig"
        }
        return mapping.get(language, language)

    def _get_compile_command(self, language: str) -> Tuple[str, str]:
        """Get compile/run command for language

        Returns: (description, command)
        """
        commands = {
            "c-c++": ("C/C++ (compile + run)", "<Space>r or :!g++ % -o main && ./main"),
            "rust": ("Rust", "<Space>r or :!rustc % -o main && ./main"),
            "python": ("Python", "<Space>r or :!python3 %"),
            "javascript": ("JavaScript", "<Space>r or :!node %"),
            "typescript": ("TypeScript", "<Space>r or :!ts-node %"),
            "go": ("Go", "<Space>r or :!go run %"),
            "lua": ("Lua", "<Space>r or :!lua %"),
            "dart": ("Dart", "<Space>r or :!dart %"),
            "swift": ("Swift", "<Space>r or :!swift %"),
            "kotlin": ("Kotlin", "<Space>r or :!kotlinc % -include-runtime -d main.jar && java -jar main.jar"),
            "sql": ("SQL", "<Space>r or :!sqlite3 < %"),
            "c#": ("C#", "<Space>r or :!csc % && mono %.exe"),
            "csharp": ("C#", "<Space>r or :!csc % && mono %.exe"),
            "shell": ("Shell", "<Space>r or :!bash %"),
            "powershell": ("PowerShell", "<Space>r or :!powershell -File %"),
            "zig": ("Zig", "<Space>r or :!zig build-exe % && ./main"),
        }
        lang_desc, cmd = commands.get(language, ("Unknown", ":!echo 'Language not configured'"))
        return lang_desc, cmd

    def _get_help_comment(self, language: str) -> str:
        """Get the help comment template for each language"""
        templates = {
            "c-c++": "// Press <Esc> <Space> h for help.\n\n\n",
            "rust": "// Press <Esc> <Space> h for help.\n\n\n",
            "python": "# Press <Esc> <Space> h for help.\n\n\n",
            "javascript": "// Press <Esc> <Space> h for help.\n\n\n",
            "typescript": "// Press <Esc> <Space> h for help.\n\n\n",
            "go": "// Press <Esc> <Space> h for help.\n\n\n",
            "lua": "-- Press <Esc> <Space> h for help.\n\n\n",
            "dart": "// Press <Esc> <Space> h for help.\n\n\n",
            "swift": "// Press <Esc> <Space> h for help.\n\n\n",
            "kotlin": "// Press <Esc> <Space> h for help.\n\n\n",
            "sql": "-- Press <Esc> <Space> h for help.\n\n\n",
            "c#": "// Press <Esc> <Space> h for help.\n\n\n",
            "csharp": "// Press <Esc> <Space> h for help.\n\n\n",
            "shell": "# Press <Esc> <Space> h for help.\n\n\n",
            "powershell": "# Press <Esc> <Space> h for help.\n\n\n",
            "zig": "// Press <Esc> <Space> h for help.\n\n\n",
        }
        return templates.get(language, "// Press <Esc> <Space> h for help.\n\n\n")

    def _create_cpp_workspace(self, workspace_dir: Path):
        """Create C++ workspace with Makefile and .clang-format"""
        main_cpp = workspace_dir / "main.cpp"
        main_cpp.write_text(self._get_help_comment("c-c++"))

        makefile = workspace_dir / "Makefile"
        makefile.write_text("""CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

TARGET = main
SRC = main.cpp

all: $(TARGET)

$(TARGET): $(SRC)
\t$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

run: $(TARGET)
\t./$(TARGET)

clean:
\trm -f $(TARGET)

.PHONY: all run clean
""")

        clang_format = workspace_dir / ".clang-format"
        clang_format.write_text("""BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
""")

    def _create_rust_workspace(self, workspace_dir: Path):
        """Create Rust workspace with Cargo.toml"""
        main_rs = workspace_dir / "main.rs"
        main_rs.write_text(self._get_help_comment("rust"))

        cargo_toml = workspace_dir / "Cargo.toml"
        cargo_toml.write_text("""[package]
name = "lesson"
version = "0.1.0"
edition = "2021"

[dependencies]
""")

    def _create_python_workspace(self, workspace_dir: Path):
        """Create Python workspace"""
        main_py = workspace_dir / "main.py"
        main_py.write_text(self._get_help_comment("python"))

    def _create_js_workspace(self, workspace_dir: Path):
        """Create JavaScript workspace"""
        main_js = workspace_dir / "main.js"
        main_js.write_text(self._get_help_comment("javascript"))

        package_json = workspace_dir / "package.json"
        package_json.write_text("""{
  "name": "lesson",
  "version": "1.0.0",
  "main": "main.js",
  "scripts": {
    "start": "node main.js"
  }
}
""")

    def _create_zig_workspace(self, workspace_dir: Path):
        """Create Zig workspace with blank main.zig file"""
        main_zig = workspace_dir / "main.zig"
        main_zig.write_text(self._get_help_comment("zig"))

    def _show_vim_instructions(self, workspace: Dict, language: str):
        """Show quick instructions before launching Vim"""
        lang_desc, compile_cmd = self._get_compile_command(language)

        # ANSI color codes
        CYAN = '\033[96m'
        YELLOW = '\033[93m'
        GREEN = '\033[92m'
        BOLD = '\033[1m'
        BG_BLUE = '\033[44m'
        BG_CYAN = '\033[46m'
        RESET = '\033[0m'

        print("\n" + "="*70)
        print("  LAUNCHING VIM LEARNING MODE")
        print("="*70)
        print(f"\n{BG_CYAN}{BOLD} QUICK GUIDE POPUP {RESET}")
        print(f"{CYAN}{BOLD}    <Space>g{RESET}           -> {YELLOW}Beautiful popup with ALL shortcuts!{RESET}")
        print("")
        print("ESSENTIAL SHORTCUTS:\n")
        print("  Windows:")
        print("    Ctrl-w h / Ctrl-w l    -> Switch between lesson and code")
        print("    Ctrl-w =           -> Balance window sizes")
        print("")
        print("  Lesson Navigation:")
        print("    j / k              -> Scroll down/up")
        print("    Ctrl-d / Ctrl-u    -> Page down/up")
        print("    gg / G             -> Jump to top/bottom")
        print("")
        print("  Editing (in code window):")
        print("    i                  -> Insert mode")
        print("    Esc                -> Return to normal mode")
        print("    :w                 -> Save file")
        print("    :q                 -> Quit")
        print("")
        print("  Compile/Run (in code window):")
        print(f"    {compile_cmd:<20} -> {lang_desc}")
        print("")
        print(f"Your code: {workspace['main_file']}")
        print("TIP: Lesson is on the LEFT, your code is on the RIGHT")
        print("")
        print(f"{GREEN}[TIP] Remember: Press {CYAN}{BOLD}<Space>g{RESET}{GREEN} anytime for the complete guide!{RESET}")
        print("="*70)
        print("\nPress ENTER to launch Vim...")
        input()

    def open_vscode(self, lesson_path: Path, language: str):
        """Open lesson in VS Code"""
        level_dir = lesson_path.parent
        subprocess.run(["code", str(level_dir)])

    def open_terminal(self, lesson_path: Path):
        """Open lesson in terminal"""
        subprocess.run(["less", "-R", str(lesson_path)])

    def _create_solution_template(self, path: Path, language: str):
        """Create file with help comment for students"""
        # Start with help comment so students know how to get assistance
        with open(path, 'w') as f:
            f.write(self._get_help_comment(language))


class InteractiveTutorial:
    """Interactive tutorial system for learning CLI features"""

    def __init__(self):
        self.current_step = 0
        self.steps = [
            self._intro,
            self._navigation_basics,
            self._lesson_structure,
            self._vim_mode_tutorial,
            self._progress_tracking,
            self._advanced_features,
            self._completion
        ]

    def run(self):
        """Run the interactive tutorial"""
        while self.current_step < len(self.steps):
            self._clear_screen()
            self.steps[self.current_step]()

            if self.current_step < len(self.steps) - 1:
                choice = input("\n→ Press Enter to continue (or 'q' to quit tutorial): ").strip().lower()
                if choice == 'q':
                    print("\nTutorial ended. You can restart anytime with option 8!")
                    input("Press Enter to return to main menu...")
                    return

            self.current_step += 1

    def _clear_screen(self):
        if utils:
            utils.clear_screen()
        else:
            os.system('clear' if os.name != 'nt' else 'cls')

    def _intro(self):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("◽ INTERACTIVE TUTORIAL")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\nThis tutorial will teach you how to use the Learn CLI effectively.")
        print("\n── What you'll learn")
        print("  · How to navigate the CLI")
        print("  · Understanding lesson structure")
        print("  · Using Vim mode efficiently")
        print("  · Tracking your progress")
        print("  · Advanced features and tips")
        print("\n[Estimated time: 5 minutes]")

    def _navigation_basics(self):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("STEP 1: NAVIGATION BASICS")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\n── The Main Menu")
        print("\nWhen you run 'learn', you see the main menu with these options:\n")
        print("  1  Start a lesson     · Begin learning a specific lesson")
        print("  2  Continue           · Pick up where you left off")
        print("  3  View progress      · See your completion status")
        print("  4  Browse all         · Explore all available lessons")
        print("  5  Switch language    · Change programming language")
        print("  6  Mark complete      · Flag a lesson as done")
        print("  7  Statistics         · View detailed stats")
        print("  8  Tutorial           · You're here now!")
        print("\n[TIP] You can also use command-line arguments:")
        print("  learn c++ 1           · Directly open C++ Stage 1, Level 1")
        print("  learn --list          · List all lessons")
        print("  learn --next          → Get next lesson suggestion")

    def _lesson_structure(self):
        print("=" * 70)
        print("  STEP 2: LESSON STRUCTURE")
        print("=" * 70)
        print("\n── How Lessons Are Organized\n")
        print("Each programming language has 5 STAGES of learning:")
        print("\n  Stage 1: Copying Code")
        print("    → Learn by following examples exactly")
        print("    → Build muscle memory and syntax familiarity")
        print("\n  Stage 2: Pseudocode to Code")
        print("    → Translate logical descriptions into code")
        print("    → Strengthen problem-solving skills")
        print("\n  Stage 3: Problem to Pseudocode")
        print("    → Design solutions before coding")
        print("    → Develop algorithmic thinking")
        print("\n  Stage 4: Full Problem Solving")
        print("    → Complete autonomy in solving problems")
        print("    → Real-world challenges")
        print("\n  Stage 5: Capstone Projects")
        print("    → Professional-level projects")
        print("    → Portfolio-worthy work")
        print("\n[NOTE] Each stage has 7 LEVELS (lessons) to complete.")

    def _vim_mode_tutorial(self):
        print("=" * 70)
        print("  STEP 3: VIM MODE (DEFAULT)")
        print("=" * 70)
        print("\n── When you open a lesson, you'll see a SPLIT-SCREEN view:\n")
        print("  ┌──────────────────┬──────────────────┐")
        print("  │                  │                  │")
        print("  │  LESSON TEXT     │  YOUR CODE       │")
        print("  │  (Read-only)     │  (Editable)      │")
        print("  │                  │                  │")
        print("  └──────────────────┴──────────────────┘")
        print("\n── Essential Vim Commands\n")
        print("  NAVIGATION:")
        print("    Ctrl-w h / Ctrl-w l    → Switch between windows")
        print("    j / k              → Move down/up")
        print("    Ctrl-d / Ctrl-u    → Page down/up")
        print("    gg / G             → Jump to top/bottom")
        print("\n  EDITING (in code window):")
        print("    i                  → Enter INSERT mode (start typing)")
        print("    Esc                → Return to NORMAL mode")
        print("    :w                 → Save your code")
        print("    :wq                → Save and quit")
        print("    :q!                → Quit without saving")
        print("\n  HELP:")
        print("    <Space>?           → Show full help in Vim")
        print("\n[TIP] Your LazyVim config is active, so you have:")
        print("  • LSP autocomplete (clangd, rust-analyzer, etc.)")
        print("  • Auto-formatting on save")
        print("  • Syntax highlighting")
        print("  • All your custom keybindings")

    def _progress_tracking(self):
        print("=" * 70)
        print("  STEP 4: PROGRESS TRACKING")
        print("=" * 70)
        print("\nYour progress is automatically tracked!\n")
        print("  • Every lesson you open is recorded")
        print("  • You can mark lessons as 'completed'")
        print("  • View stats anytime with option 3 or 7")
        print("\n── Marking Lessons Complete\n")
        print("  From the main menu:")
        print("    → Select option 6 (Mark lesson as complete)")
        print("    → Enter: language, stage, level")
        print("\n  From command line:")
        print("    learn --complete c++ 1 1")
        print("\n── Progress is saved in: .learn-progress.json")
        print("\n[TIP] Use 'learn --next' to get a suggestion for")
        print("         what to study next based on your progress!")

    def _advanced_features(self):
        print("=" * 70)
        print("  STEP 5: ADVANCED FEATURES")
        print("=" * 70)
        print("\n── Power User Tips:\n")
        print("  COMMAND-LINE SHORTCUTS:")
        print("    learn c++ 3 --stage 2     → Open specific stage/level")
        print("    learn --list              → Quick lesson browser")
        print("    learn --progress          → Quick progress check")
        print("\n  EDITOR MODES:")
        print("    learn c++ 1 --vim         → Open in Vim (default)")
        print("    learn c++ 1 --vscode      → Open in VS Code")
        print("    learn c++ 1 --terminal    → Read-only terminal view")
        print("\n  MULTIPLE LANGUAGES:")
        print("    • C/C++")
        print("    • Rust")
        print("    • Python")
        print("    • JavaScript")
        print("    • Go")
        print("    • Lua")
        print("\n  WORKFLOW TIPS:")
        print("    1. Start with 'learn --list' to see all lessons")
        print("    2. Begin at Stage 1, Level 1 for any language")
        print("    3. Complete levels sequentially for best results")
        print("    4. Mark lessons complete to track progress")
        print("    5. Use 'learn --next' when unsure what to do")
        print("\n── SETUP COMPLETE:")
        print("  • Full LSP support (autocomplete, diagnostics)")
        print("  • Auto-formatting on save")
        print("  • 9 formatters & LSPs installed via Mason")

    def _completion(self):
        print("=" * 70)
        print("  ◽ TUTORIAL COMPLETE")
        print("=" * 70)
        print("\nYou're now ready to start learning!\n")
        print("── Quick Reference Card\n")
        print("  Start learning:     learn c++ 1")
        print("  Continue:           learn --next")
        print("  List lessons:       learn --list")
        print("  Check progress:     learn --progress")
        print("  Get help:           learn --help")
        print("\n── Recommended First Steps")
        print("  1. Run: learn c++ 1")
        print("  2. Practice Vim navigation (Ctrl-h/l)")
        print("  3. Complete the lesson")
        print("  4. Mark it complete: learn --complete c++ 1 1")
        print("  5. Continue to next lesson: learn --next")
        print("\nHappy Learning!")
        input("\nPress Enter to return to main menu...")


class InteractiveCLI:
    """Interactive CLI interface"""

    def __init__(self, learn_dir: Path):
        self.learn_dir = learn_dir
        self.progress = ProgressTracker(learn_dir)
        self.lesson_mgr = LessonManager(learn_dir)
        self.executor = LessonExecutor(self.lesson_mgr)

    def run_interactive_mode(self):
        """Run interactive menu"""
        while True:
            self._clear_screen()
            self._print_header()
            self._print_status_bar()
            self._print_main_menu()
            self._print_recent_lessons()
            self._print_footer_hint(["[0] quit", "[h] help"])

            choice = input("\n→ Select option: ").strip()

            if choice == "1":
                self._select_language_and_lesson()
            elif choice == "2":
                self._continue_learning()
            elif choice == "3":
                self._view_progress()
            elif choice == "4":
                self._browse_all_lessons()
            elif choice == "8":
                self._run_tutorial()
            elif choice == "5":
                self._switch_language()
            elif choice == "6":
                self._mark_lesson_complete()
            elif choice == "7":
                self._view_stats()
            elif choice == "9":
                self._system_diagnostics()
            elif choice == "q" or choice == "0":
                print("\nHappy learning!")
                break
            else:
                print("Invalid option. Press Enter to continue...")
                input()

    def _clear_screen(self):
        """Clear terminal screen"""
        if console:
            console.clear()
        elif utils:
            utils.clear_screen()
        else:
            os.system('clear' if os.name != 'nt' else 'cls')

    def _print_header(self, context: str = ""):
        """Print CLI header with optional context breadcrumbs"""
        if console:
            console.print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
            console.print("[bold cyan]◽ LEARN CLI[/bold cyan]")
            if context:
                console.print(f"[dim]   {context}[/dim]")
            else:
                console.print("[dim]   Interactive Programming Learning[/dim]")
            console.print("[bold cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/bold cyan]")
        else:
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("◽ LEARN CLI")
            if context:
                print(f"   {context}")
            else:
                print("   Interactive Programming Learning")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def _print_footer_hint(self, hints: List[str]):
        """Show contextual keyboard hints at bottom of screen"""
        if console:
            hint_text = " · ".join([f"[dim]{h}[/dim]" for h in hints])
            console.print(f"\n[dim]─────────────────────────────────────[/dim]")
            console.print(f"  {hint_text}")
        else:
            hint_text = " · ".join(hints)
            print(f"\n─────────────────────────────────────")
            print(f"  {hint_text}")

    def _print_status_bar(self):
        """Show current status at top of screen"""
        total_completed = sum(
            self.progress.get_completion_stats(lang)["completed"]
            for lang in self.lesson_mgr.languages.keys()
        )
        active_langs = len([lang for lang in self.progress.data.get("languages", {}).values() if lang.get("sessions")])

        if console:
            console.print(f"[dim]Lessons completed: {total_completed} · Active languages: {active_langs}[/dim]\n")
        else:
            print(f"Lessons completed: {total_completed} · Active languages: {active_langs}\n")

    def _print_recent_lessons(self):
        """Show 3 most recent lessons in main menu"""
        all_sessions = []
        for lang, lang_data in self.progress.data.get("languages", {}).items():
            for session in lang_data.get("sessions", []):
                all_sessions.append({
                    "language": lang,
                    "stage": session.get("stage"),
                    "level": session.get("level"),
                    "last_opened": session.get("last_opened", "")
                })

        # Sort by last_opened and get top 3
        all_sessions.sort(key=lambda x: x.get("last_opened", ""), reverse=True)
        recent = all_sessions[:3]

        if recent:
            if console:
                console.print("\n[dim]Recent lessons:[/dim]")
                for idx, session in enumerate(recent, 1):
                    lang = session["language"]
                    display_name = self.lesson_mgr.get_language_display_name(lang)
                    console.print(f"  [dim]{idx}.[/dim] [cyan]{display_name}[/cyan] [dim]· Stage {session['stage']}, Level {session['level']}[/dim]")
            else:
                print("\nRecent lessons:")
                for idx, session in enumerate(recent, 1):
                    lang = session["language"]
                    display_name = self.lesson_mgr.get_language_display_name(lang)
                    print(f"  {idx}. {display_name} · Stage {session['stage']}, Level {session['level']}")

    def _get_input_with_shortcuts(self, prompt: str, allow_back: bool = True, allow_help: bool = True) -> str:
        """Enhanced input with global shortcuts (q=quit, b=back, h=help)"""
        choice = input(prompt).strip().lower()

        if choice == 'q':
            if console:
                console.print("\n[dim]Returning to main menu...[/dim]")
            else:
                print("\nReturning to main menu...")
            return 'QUIT'
        elif choice == 'b' and allow_back:
            return 'BACK'
        elif choice == 'h' and allow_help:
            self._show_contextual_help()
            return self._get_input_with_shortcuts(prompt, allow_back, allow_help)

        return choice

    def _show_contextual_help(self):
        """Show contextual help"""
        if console:
            console.print("\n[bold cyan]◽ QUICK HELP[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]")
            console.print("  [cyan]q[/cyan]  Return to main menu")
            console.print("  [cyan]b[/cyan]  Go back one level")
            console.print("  [cyan]h[/cyan]  Show this help")
            console.print("  [cyan]0[/cyan]  Exit application")
        else:
            print("\n◽ QUICK HELP")
            print("─────────────────────────────────────")
            print("  q  Return to main menu")
            print("  b  Go back one level")
            print("  h  Show this help")
            print("  0  Exit application")
        input("\nPress Enter to continue...")

    def _show_lesson_preview(self, lesson_path: Path) -> bool:
        """Show first 5 lines of lesson. Returns True if user wants to open it."""
        try:
            with open(lesson_path, 'r', encoding='utf-8') as f:
                lines = [line.rstrip() for line in f.readlines()[:5]]

            if console:
                console.print("\n[dim]Preview:[/dim]")
                for line in lines:
                    console.print(f"  [dim]{line}[/dim]")
                console.print("  [dim]...[/dim]\n")
            else:
                print("\nPreview:")
                for line in lines:
                    print(f"  {line}")
                print("  ...\n")

            choice = input("→ Open this lesson? (Y/n): ").strip().lower()
            return choice != 'n'
        except Exception as e:
            if console:
                console.print(f"[yellow][!!] Could not preview: {e}[/yellow]")
            else:
                print(f"[!!] Could not preview: {e}")
            return True  # Default to opening if preview fails

    def _print_main_menu(self):
        """Print main menu"""
        if console:
            console.print("\n[bold cyan]◽ MAIN MENU[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")
            menu_items = [
                "  [cyan]1[/cyan]  Start a lesson",
                "  [cyan]2[/cyan]  Continue learning",
                "  [cyan]3[/cyan]  View progress",
                "  [cyan]4[/cyan]  Browse all lessons",
                "  [cyan]5[/cyan]  Switch language",
                "  [cyan]6[/cyan]  Mark lesson complete",
                "  [cyan]7[/cyan]  View statistics",
                "  [cyan]8[/cyan]  Interactive tutorial",
                "  [cyan]9[/cyan]  System diagnostics",
                "  [cyan]0[/cyan]  Exit"
            ]
            for item in menu_items:
                console.print(item)
        else:
            print("\n◽ MAIN MENU")
            print("─────────────────────────────────────\n")
            print("  1  Start a lesson")
            print("  2  Continue learning")
            print("  3  View progress")
            print("  4  Browse all lessons")
            print("  5  Switch language")
            print("  6  Mark lesson complete")
            print("  7  View statistics")
            print("  8  Interactive tutorial")
            print("  9  System diagnostics")
            print("  0  Exit")

    def _select_language_and_lesson(self):
        """Select language and lesson interactively - now with categories"""
        self._clear_screen()
        if console:
            console.print("\n[bold cyan]◽ SELECT CATEGORY[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")
        else:
            print("\n◽ SELECT CATEGORY")
            print("─────────────────────────────────────\n")

        # Show categories
        categories = [
            ("1", "Core Languages", ["c-c++", "rust", "go", "zig"]),
            ("2", "Web & Scripting", ["javascript", "typescript", "python", "php"]),
            ("3", "Mobile Development", ["swift", "kotlin", "dart"]),
            ("4", "Data & Databases", ["sql", "nosql", "r", "julia"]),
            ("5", "Scripting & Automation", ["shell", "powershell", "lua"]),
            ("6", "Enterprise & Systems", ["java", "csharp"]),
            ("7", "All Languages", None)
        ]

        for num, name, _ in categories:
            if console:
                console.print(f"  [cyan]{num}.[/cyan] {name}")
            else:
                print(f"  {num}. {name}")

        category_choice = input("\n→ Select category (or 'b' to go back): ").strip()

        if category_choice.lower() == 'b':
            return

        # Find selected category
        selected_languages = None
        for num, name, langs in categories:
            if category_choice == num:
                selected_languages = langs
                break

        if selected_languages is None and category_choice == "7":
            # Show all languages
            selected_languages = list(self.lesson_mgr.languages.keys())
        elif selected_languages is None:
            if console:
                console.print("[yellow][!!] Please enter 1-7 or 'b' to go back[/yellow]")
            else:
                print("[!!] Please enter 1-7 or 'b' to go back")
            input("Press Enter to try again...")
            return

        # Now show languages from selected category
        self._clear_screen()
        if console:
            console.print("\n[bold cyan]◽ SELECT LANGUAGE[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")
        else:
            print("\n◽ SELECT LANGUAGE")
            print("─────────────────────────────────────\n")

        for idx, lang in enumerate(selected_languages, 1):
            display_name = self.lesson_mgr.get_language_display_name(lang)
            stats = self.progress.get_completion_stats(lang)

            if stats["completed"] > 0:
                pct = stats["percentage"]
                if console:
                    console.print(f"  [cyan]{idx}.[/cyan] {display_name} [dim]({pct:.0f}% complete)[/dim]")
                else:
                    print(f"  {idx}. {display_name} ({pct:.0f}% complete)")
            else:
                if console:
                    console.print(f"  [cyan]{idx}.[/cyan] {display_name}")
                else:
                    print(f"  {idx}. {display_name}")

        lang_choice = input("\n→ Select language (or 'b' to go back): ").strip()

        if lang_choice.lower() == 'b':
            # Go back to category selection
            self._select_language_and_lesson()
            return

        try:
            lang_idx = int(lang_choice) - 1
            if 0 <= lang_idx < len(selected_languages):
                language = selected_languages[lang_idx]
                self._select_stage_and_level(language)
            else:
                if console:
                    console.print(f"[yellow][!!] Please enter 1-{len(selected_languages)} or 'b' to go back[/yellow]")
                else:
                    print(f"[!!] Please enter 1-{len(selected_languages)} or 'b' to go back")
                input("Press Enter to try again...")
        except ValueError:
            if console:
                console.print(f"[yellow][!!] Please enter 1-{len(selected_languages)} or 'b' to go back[/yellow]")
            else:
                print(f"[!!] Please enter 1-{len(selected_languages)} or 'b' to go back")
            input("Press Enter to try again...")

    def _select_stage_and_level(self, language: str):
        """Select stage and level"""
        self._clear_screen()
        display_name = self.lesson_mgr.get_language_display_name(language)
        print(f"◽ {display_name.upper()} - SELECT LESSON\n")

        print("  Stage:")
        for i in range(1, 6):
            print(f"    {i}. Stage {i}")

        stage = input("\n→ Enter stage (1-5): ").strip()

        try:
            stage = int(stage)
            if 1 <= stage <= 5:
                level = input("→ Enter level (1-7): ").strip()
                level = int(level)

                if 1 <= level <= 7:
                    self._open_lesson(language, stage, level)
        except ValueError:
            print("Invalid input!")
            input("Press Enter to continue...")

    def _open_lesson(self, language: str, stage: int, level: int, mode: str = None):
        """Open a lesson"""
        lesson_path = self.lesson_mgr.find_lesson(language, stage, level)

        if not lesson_path:
            print(f"\n[!!] Lesson not found: Stage {stage}, Level {level}")
            input("Press Enter to continue...")
            return

        # Show preview and confirm
        if not self._show_lesson_preview(lesson_path):
            return

        # Check if language runtime is available
        checker = SystemChecker()
        is_available, runtime_name, install_cmd = checker.check_language_runtime(language)

        if not is_available:
            self._clear_screen()
            if console:
                console.print("\n[bold red]◽ RUNTIME NOT FOUND[/bold red]")
                console.print("[dim]─────────────────────────────────────[/dim]\n")
                console.print(f"[bold yellow]{runtime_name}[/bold yellow] is required to run {language} lessons.\n")
                console.print(f"[dim]Install with:[/dim]")
                console.print(f"  [cyan]{install_cmd}[/cyan]\n")
                console.print("[dim]Or select Option 9 from the main menu to install all dependencies.[/dim]")
            else:
                print("\n◽ RUNTIME NOT FOUND")
                print("─────────────────────────────────────")
                print(f"\n{runtime_name} is required to run {language} lessons.\n")
                print(f"Install with:\n  {install_cmd}\n")
                print("Or select Option 9 from the main menu to install all dependencies.")

            input("\nPress Enter to continue...")
            return

        if mode is None:
            mode = self._select_mode()

        if mode:
            self.progress.mark_lesson_opened(language, stage, level, mode)

            if mode == "vim":
                self.executor.open_vim(lesson_path, language)
            elif mode == "vscode":
                self.executor.open_vscode(lesson_path, language)
            elif mode == "terminal":
                self.executor.open_terminal(lesson_path)

    def _select_mode(self) -> Optional[str]:
        """Select editor mode"""
        print("\n◽ SELECT MODE\n")
        print("  1. Vim (default)")
        print("  2. VS Code")
        print("  3. Terminal (read-only)")
        print("  b. Back")

        choice = input("\n→ Select mode: ").strip()

        if choice == "1" or choice == "":
            return "vim"
        elif choice == "2":
            return "vscode"
        elif choice == "3":
            return "terminal"
        else:
            return None

    def _continue_learning(self):
        """Continue from last lesson"""
        sessions = self.progress.data.get("sessions", [])

        if not sessions:
            print("\nNo previous sessions found. Start with a new lesson!")
            input("Press Enter to continue...")
            return

        last_session = sessions[-1]
        language = last_session["language"]

        next_lesson = self.progress.get_next_lesson(language)

        if next_lesson:
            stage, level = next_lesson
            display_name = self.lesson_mgr.get_language_display_name(language)

            print(f"\n◽ Next lesson: {display_name} - Stage {stage}, Level {level}")
            confirm = input("→ Open this lesson? (Y/n): ").strip().lower()

            if confirm != 'n':
                self._open_lesson(language, stage, level)
        else:
            print(f"\n[OK] Congratulations! You've completed all lessons in {language}!")
            input("Press Enter to continue...")

    def _view_progress(self):
        """View learning progress"""
        self._clear_screen()
        if console:
            console.print("\n[bold cyan]◽ PROGRESS[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")

            table = Table(show_header=True, header_style="bold cyan", box=None)
            table.add_column("Language", style="cyan")
            table.add_column("Completed", style="dim white")
            table.add_column("Total", style="dim white")
            table.add_column("Progress", style="cyan")

            for language in self.lesson_mgr.languages.keys():
                display_name = self.lesson_mgr.get_language_display_name(language)
                stats = self.progress.get_completion_stats(language)

                if stats["completed"] > 0:
                    bar_length = 20
                    filled = int(stats['percentage'] / 100 * bar_length)
                    bar = "█" * filled + "░" * (bar_length - filled)
                    progress_str = f"{bar} {stats['percentage']:.0f}%"

                    table.add_row(
                        display_name,
                        str(stats['completed']),
                        str(stats['total']),
                        progress_str
                    )

            console.print(table)

            sessions = self.progress.data.get("sessions", [])
            if sessions:
                console.print(f"\n[dim]Total sessions:[/dim] [cyan]{len(sessions)}[/cyan]")

                last_session = sessions[-1]
                lang_display = self.lesson_mgr.get_language_display_name(last_session["language"])
                console.print(f"[dim]Last session:[/dim] [cyan]{lang_display} · Stage {last_session['stage']} · Level {last_session['level']}[/cyan]")
        else:
            print("\n◽ PROGRESS")
            print("─────────────────────────────────────\n")

            for language in self.lesson_mgr.languages.keys():
                display_name = self.lesson_mgr.get_language_display_name(language)
                stats = self.progress.get_completion_stats(language)

                if stats["completed"] > 0:
                    print(f"\n{display_name}:")
                    print(f"  Completed: {stats['completed']}/{stats['total']} lessons")
                    print(f"  Progress: {stats['percentage']:.1f}%")

                    bar_length = 30
                    filled = int(stats['percentage'] / 100 * bar_length)
                    bar = "█" * filled + "░" * (bar_length - filled)
                    print(f"  [{bar}]")

            sessions = self.progress.data.get("sessions", [])
            if sessions:
                print(f"\nTotal sessions: {len(sessions)}")

                last_session = sessions[-1]
                lang_display = self.lesson_mgr.get_language_display_name(last_session["language"])
                print(f"Last session: {lang_display} - Stage {last_session['stage']}, Level {last_session['level']}")

        input("\nPress Enter to continue...")

    def _browse_all_lessons(self):
        """Browse all available lessons"""
        self._clear_screen()
        if console:
            console.print("\n[bold cyan]◽ LESSONS[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")

            # Ask for filter
            console.print("[dim]Filter:[/dim]")
            console.print("  [cyan]1[/cyan] All lessons")
            console.print("  [cyan]2[/cyan] In progress")
            console.print("  [cyan]3[/cyan] Not started")
            console.print("  [cyan]4[/cyan] Completed\n")

            filter_choice = input("→ Select filter (default: 1): ").strip() or "1"

            self._clear_screen()
            console.print("\n[bold cyan]◽ LESSONS[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")

            lessons = self.lesson_mgr.list_all_lessons()

            for lang_code, stages in lessons.items():
                display_name = self.lesson_mgr.get_language_display_name(lang_code)
                console.print(f"\n[bold cyan]{display_name}[/bold cyan]")
                console.print("[dim]" + "─" * 60 + "[/dim]")

                for stage, levels in stages.items():
                    if levels:
                        # Apply filter
                        filtered_levels = []
                        for level in levels:
                            lang_data = self.progress.data.get("languages", {}).get(lang_code, {})
                            completed = lang_data.get("completed", [])
                            is_completed = any(c["stage"] == stage and c["level"] == level for c in completed)
                            sessions = lang_data.get("sessions", [])
                            is_in_progress = any(s["stage"] == stage and s["level"] == level for s in sessions)

                            if filter_choice == "1":  # All
                                filtered_levels.append((level, is_completed, is_in_progress))
                            elif filter_choice == "2" and is_in_progress and not is_completed:  # In progress
                                filtered_levels.append((level, is_completed, is_in_progress))
                            elif filter_choice == "3" and not is_in_progress and not is_completed:  # Not started
                                filtered_levels.append((level, is_completed, is_in_progress))
                            elif filter_choice == "4" and is_completed:  # Completed
                                filtered_levels.append((level, is_completed, is_in_progress))

                        if filtered_levels:
                            levels_str = ", ".join([
                                f"[green]{l}[/green]" if completed else
                                f"[yellow]{l}[/yellow]" if in_progress else
                                f"[cyan]{l}[/cyan]"
                                for l, completed, in_progress in filtered_levels
                            ])
                            console.print(f"  [dim]Stage {stage}:[/dim] {levels_str}")
        else:
            print("\n◽ LESSONS")
            print("─────────────────────────────────────\n")

            lessons = self.lesson_mgr.list_all_lessons()

            for lang_code, stages in lessons.items():
                display_name = self.lesson_mgr.get_language_display_name(lang_code)
                print(f"\n{display_name}")
                print("=" * 50)

                for stage, levels in stages.items():
                    if levels:
                        print(f"  Stage {stage}: Levels {', '.join(map(str, levels))}")

        input("\nPress Enter to continue...")

    def _switch_language(self):
        """Switch to a different language"""
        self._select_language_and_lesson()

    def _mark_lesson_complete(self):
        """Mark a lesson as completed"""
        self._clear_screen()
        if console:
            console.print(Panel.fit(
                "[bold cyan]◽ MARK LESSON COMPLETE[/bold cyan]",
                border_style="cyan"
            ))
            console.print()
        else:
            print("◽ MARK LESSON COMPLETE\n")

        languages = list(self.lesson_mgr.languages.keys())
        for idx, lang in enumerate(languages, 1):
            display_name = self.lesson_mgr.get_language_display_name(lang)
            if console:
                console.print(f"  [cyan]{idx}.[/cyan] {display_name}")
            else:
                print(f"  {idx}. {display_name}")

        lang_choice = input("\n→ Select language: ").strip()

        try:
            lang_idx = int(lang_choice) - 1
            if 0 <= lang_idx < len(languages):
                language = languages[lang_idx]

                stage = int(input("→ Stage number (1-5): ").strip())
                level = int(input("→ Level number (1-7): ").strip())

                # Show confirmation
                display_name = self.lesson_mgr.get_language_display_name(language)
                if console:
                    console.print(f"\n[yellow]This will mark as complete:[/yellow]")
                    console.print(f"  [cyan]{display_name}[/cyan] → Stage {stage}, Level {level}")
                    console.print(f"\n[dim]You can still reopen it anytime[/dim]")
                else:
                    print(f"\nThis will mark as complete:")
                    print(f"  {display_name} → Stage {stage}, Level {level}")
                    print(f"\nYou can still reopen it anytime")

                confirm = input("\n→ Confirm? (y/N): ").strip().lower()
                if confirm != 'y':
                    if console:
                        console.print("[dim]Cancelled[/dim]")
                    else:
                        print("Cancelled")
                    input("Press Enter to continue...")
                    return

                if self.progress.mark_lesson_completed(language, stage, level):
                    if console:
                        console.print(f"\n[bold green]◽ Lesson marked as complete![/bold green]")
                    else:
                        print(f"\n[OK] Lesson marked as complete!")
                else:
                    if console:
                        console.print(f"\n[bold red][!!] Lesson not found in progress.[/bold red]")
                    else:
                        print(f"\n[!!] Lesson not found in progress.")
        except ValueError:
            if console:
                console.print("[bold red]Invalid input![/bold red]")
            else:
                print("Invalid input!")

        input("Press Enter to continue...")

    def _view_stats(self):
        """View detailed statistics"""
        self._clear_screen()
        if console:
            console.print("\n[bold cyan]◽ STATISTICS[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")

            total_lessons = 0
            total_completed = 0

            for language in self.lesson_mgr.languages.keys():
                stats = self.progress.get_completion_stats(language)
                total_lessons += stats["total"]
                total_completed += stats["completed"]

            stats_text = Text()
            stats_text.append(f"Total lessons available: ", style="dim")
            stats_text.append(f"{total_lessons}\n", style="bold yellow")
            stats_text.append(f"Lessons completed: ", style="dim")
            stats_text.append(f"{total_completed}\n", style="bold green")

            if total_lessons > 0:
                overall_pct = (total_completed / total_lessons * 100)
                bar_length = 30
                filled = int(overall_pct / 100 * bar_length)
                bar = "█" * filled + "░" * (bar_length - filled)
                stats_text.append(f"Completion rate: ", style="dim")
                stats_text.append(f"{overall_pct:.1f}%\n", style="bold green")
                stats_text.append(f"[{bar}]\n", style="green")

            sessions = self.progress.data.get("sessions", [])
            stats_text.append(f"Total study sessions: ", style="dim")
            stats_text.append(f"{len(sessions)}\n", style="bold yellow")

            if sessions:
                first_session = sessions[0]["timestamp"]
                stats_text.append(f"Started learning: ", style="dim")
                stats_text.append(f"{first_session[:10]}", style="bold cyan")

            console.print(stats_text)
        else:
            print("DETAILED STATISTICS\n")

            total_lessons = 0
            total_completed = 0

            for language in self.lesson_mgr.languages.keys():
                stats = self.progress.get_completion_stats(language)
                total_lessons += stats["total"]
                total_completed += stats["completed"]

            print(f"Overall Progress:")
            print(f"  Total lessons available: {total_lessons}")
            print(f"  Lessons completed: {total_completed}")

            if total_lessons > 0:
                overall_pct = (total_completed / total_lessons * 100)
                print(f"  Completion rate: {overall_pct:.1f}%")

            sessions = self.progress.data.get("sessions", [])
            print(f"\nSession Statistics:")
            print(f"  Total study sessions: {len(sessions)}")

            if sessions:
                first_session = sessions[0]["timestamp"]
                print(f"  Started learning: {first_session[:10]}")

        input("\nPress Enter to continue...")

    def _run_tutorial(self):
        """Run the interactive tutorial"""
        tutorial = InteractiveTutorial()
        tutorial.run()

    def _system_diagnostics(self):
        """System diagnostics and setup menu"""
        while True:
            self._clear_screen()
            if console:
                console.print("\n[bold cyan]◽ SYSTEM DIAGNOSTICS[/bold cyan]")
                console.print("[dim]─────────────────────────────────────[/dim]\n")
                diag_items = [
                    "  [cyan]1[/cyan]  Run system check",
                    "  [cyan]2[/cyan]  Run setup wizard",
                    "  [cyan]3[/cyan]  Reset progress",
                    "  [cyan]4[/cyan]  Show configuration",
                    "  [cyan]5[/cyan]  Install dependencies",
                    "  [cyan]6[/cyan]  Check for updates",
                    "  [cyan]7[/cyan]  Update to latest version",
                    "  [cyan]8[/cyan]  Reset all data (progress + workspaces)",
                    "  [cyan]9[/cyan]  Uninstall LEARN CLI",
                    "  [cyan]b[/cyan]  Back"
                ]
                for item in diag_items:
                    console.print(item)
            else:
                print("\n◽ SYSTEM DIAGNOSTICS")
                print("─────────────────────────────────────\n")
                print("  1  Run system check")
                print("  2  Run setup wizard")
                print("  3  Reset progress")
                print("  4  Show configuration")
                print("  5  Install dependencies")
                print("  6  Check for updates")
                print("  7  Update to latest version")
                print("  8  Reset all data (progress + workspaces)")
                print("  9  Uninstall LEARN CLI")
                print("  b  Back")

            choice = input("\n→ Select option: ").strip().lower()

            if choice == "1":
                self._clear_screen()
                checker = SystemChecker()
                checker.check_all()
                checker.print_report()
                input("\nPress Enter to continue...")

            elif choice == "2":
                wizard = InitWizard(self.learn_dir)
                wizard.run()
                break

            elif choice == "3":
                if console:
                    console.print("\n[bold yellow][!!] WARNING: This will reset all your progress![/bold yellow]")
                else:
                    print("\n[!!] WARNING: This will reset all your progress!")

                confirm = input("Are you sure? (type 'yes' to confirm): ").strip().lower()

                if confirm == "yes":
                    self.progress.data = self.progress._init_progress()
                    self.progress._save_progress()
                    if console:
                        console.print("\n[bold green][OK] Progress reset successfully[/bold green]")
                    else:
                        print("\n[OK] Progress reset successfully")
                    input("Press Enter to continue...")
                else:
                    if console:
                        console.print("\n[bold]Reset cancelled.[/bold]")
                    else:
                        print("\nReset cancelled.")
                    input("Press Enter to continue...")

            elif choice == "4":
                self._show_configuration()

            elif choice == "5":
                self._install_dependencies()

            elif choice == "6":
                # Check for updates
                self._clear_screen()
                update_info = check_for_updates(self.learn_dir)
                
                if "error" in update_info:
                    if console:
                        console.print(f"[bold red]Error:[/bold red] {update_info['error']}")
                    else:
                        print(f"Error: {update_info['error']}")
                elif update_info["has_update"]:
                    if console:
                        console.print(f"[bold yellow]Update available![/bold yellow]")
                        console.print(f"  Current: [cyan]{update_info['current']}[/cyan]")
                        console.print(f"  Latest:  [green]{update_info['latest']}[/green]")
                        console.print(f"  Commits behind: [yellow]{update_info['commits_behind']}[/yellow]")
                    else:
                        print(f"Update available!")
                        print(f"  Current: {update_info['current']}")
                        print(f"  Latest:  {update_info['latest']}")
                        print(f"  Commits behind: {update_info['commits_behind']}")
                else:
                    if console:
                        console.print(f"[bold green]✓ You're on the latest version[/bold green]")
                        console.print(f"[dim]Version: {update_info['current']}[/dim]")
                    else:
                        print(f"✓ You're on the latest version")
                        print(f"Version: {update_info['current']}")
                
                input("\nPress Enter to continue...")

            elif choice == "7":
                # Update to latest version
                self._clear_screen()
                update_learn(self.learn_dir)
                input("\nPress Enter to continue...")

            elif choice == "8":
                # Reset all data
                self._clear_screen()
                reset_user_data(self.learn_dir)
                input("\nPress Enter to continue...")

            elif choice == "9":
                # Uninstall
                self._clear_screen()
                uninstall_learn(self.learn_dir)
                # If user completes uninstall, exit the program
                if console:
                    console.print("\n[bold yellow]Exiting LEARN CLI...[/bold yellow]")
                else:
                    print("\nExiting LEARN CLI...")
                import sys
                sys.exit(0)

            elif choice == "b" or choice == "":
                break

            else:
                if console:
                    console.print("[bold red]Invalid option![/bold red]")
                else:
                    print("Invalid option!")
                input("Press Enter to continue...")

    def _show_configuration(self):
        """Show current configuration"""
        self._clear_screen()
        if console:
            console.print("\n[bold cyan]◽ CONFIGURATION[/bold cyan]")
            console.print("[dim]─────────────────────────────────────[/dim]\n")

            config_info = Text()
            config_info.append("Paths\n", style="bold cyan")
            config_info.append(f"  LEARN Directory: ", style="dim")
            config_info.append(f"{self.learn_dir}\n", style="cyan")

            workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"
            config_info.append(f"  Workspace Root: ", style="dim")
            config_info.append(f"{workspace_root}\n", style="cyan")

            progress_file = self.learn_dir / ".learn-progress.json"
            config_info.append(f"  Progress File: ", style="dim")
            config_info.append(f"{progress_file}\n", style="cyan")

            config_info.append("\nStatistics\n", style="bold cyan")
            total_sessions = len(self.progress.data.get("sessions", []))
            config_info.append(f"  Total Sessions: ", style="dim")
            config_info.append(f"{total_sessions}\n", style="cyan")

            languages_started = len(self.progress.data.get("languages", {}))
            config_info.append(f"  Languages Started: ", style="dim")
            config_info.append(f"{languages_started}\n", style="cyan")

            console.print(config_info)
        else:
            print("\n◽ CONFIGURATION")
            print("─────────────────────────────────────")

            print("\nPaths:")
            print(f"  LEARN Directory: {self.learn_dir}")

            workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"
            print(f"  Workspace Root: {workspace_root}")

            progress_file = self.learn_dir / ".learn-progress.json"
            print(f"  Progress File: {progress_file}")

            print("\nStatistics:")
            total_sessions = len(self.progress.data.get("sessions", []))
            print(f"  Total Sessions: {total_sessions}")

            languages_started = len(self.progress.data.get("languages", {}))
            print(f"  Languages Started: {languages_started}")

        input("\nPress Enter to continue...")

    def _install_dependencies(self):
        """Install/Reinstall dependencies"""
        self._clear_screen()
        checker = SystemChecker()
        checker.check_all()

        if console:
            console.print("\n[bold cyan]Installing Dependencies[/bold cyan]\n")
        else:
            print("\nInstalling Dependencies\n")

        fixes_needed = [c for c in checker.checks if c["status"] != "OK" and c.get("fix")]

        if not fixes_needed:
            if console:
                console.print("[bold green][OK] All dependencies are already installed[/bold green]")
            else:
                print("[OK] All dependencies are already installed")
            input("Press Enter to continue...")
            return

        for check in fixes_needed:
            if console:
                console.print(f"[yellow]{check['name']}[/yellow]:")
                console.print(f"  [cyan]{check['fix']}[/cyan]")
            else:
                print(f"{check['name']}:")
                print(f"  {check['fix']}")

            confirm = input("  Run this? (Y/n): ").strip().lower()
            if confirm != 'n':
                os.system(check['fix'])

        if console:
            console.print("\n[bold green][OK] Dependencies updated[/bold green]")
        else:
            print("\n[OK] Dependencies updated")

        input("Press Enter to continue...")


def check_for_updates(learn_dir: Path) -> dict:
    """Check if updates are available from GitHub
    
    Returns:
        dict with keys: has_update (bool), current (str), latest (str), commits_behind (int)
    """
    try:
        import subprocess
        
        # Get current commit hash
        result = subprocess.run(
            ["git", "-C", str(learn_dir), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5
        )
        current_hash = result.stdout.strip() if result.returncode == 0 else None
        
        # Fetch latest from remote
        subprocess.run(
            ["git", "-C", str(learn_dir), "fetch", "origin", "main"],
            capture_output=True,
            timeout=10
        )
        
        # Get remote commit hash
        result = subprocess.run(
            ["git", "-C", str(learn_dir), "rev-parse", "origin/main"],
            capture_output=True,
            text=True,
            timeout=5
        )
        remote_hash = result.stdout.strip() if result.returncode == 0 else None
        
        if not current_hash or not remote_hash:
            return {"has_update": False, "current": "unknown", "latest": "unknown", "commits_behind": 0}
        
        # Count commits behind
        result = subprocess.run(
            ["git", "-C", str(learn_dir), "rev-list", "--count", f"{current_hash}..{remote_hash}"],
            capture_output=True,
            text=True,
            timeout=5
        )
        commits_behind = int(result.stdout.strip()) if result.returncode == 0 else 0
        
        return {
            "has_update": current_hash != remote_hash,
            "current": current_hash[:7],
            "latest": remote_hash[:7],
            "commits_behind": commits_behind
        }
        
    except Exception as e:
        return {"has_update": False, "current": "error", "latest": "error", "commits_behind": 0, "error": str(e)}


def update_learn(learn_dir: Path):
    """Update LEARN to the latest version"""
    if console:
        console.print("[bold cyan]╔══════════════════════════════════════════════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║              UPDATE LEARN CLI                                ║[/bold cyan]")
        console.print("[bold cyan]╚══════════════════════════════════════════════════════════════╝[/bold cyan]")
        console.print("\n[bold]Checking for updates...[/bold]")
    else:
        print("=" * 70)
        print("  UPDATE LEARN CLI")
        print("=" * 70)
        print("\nChecking for updates...")
    
    update_info = check_for_updates(learn_dir)
    
    if "error" in update_info:
        if console:
            console.print(f"\n[bold red]Error checking for updates:[/bold red] {update_info['error']}")
        else:
            print(f"\nError checking for updates: {update_info['error']}")
        return
    
    if not update_info["has_update"]:
        if console:
            console.print("\n[bold green]✓ You're already on the latest version![/bold green]")
            console.print(f"[dim]Current version: {update_info['current']}[/dim]")
        else:
            print("\n✓ You're already on the latest version!")
            print(f"Current version: {update_info['current']}")
        return
    
    # Show update info
    if console:
        console.print(f"\n[bold yellow]Update available![/bold yellow]")
        console.print(f"  Current version: [cyan]{update_info['current']}[/cyan]")
        console.print(f"  Latest version:  [green]{update_info['latest']}[/green]")
        console.print(f"  Commits behind:  [yellow]{update_info['commits_behind']}[/yellow]")
    else:
        print(f"\nUpdate available!")
        print(f"  Current version: {update_info['current']}")
        print(f"  Latest version:  {update_info['latest']}")
        print(f"  Commits behind:  {update_info['commits_behind']}")
    
    confirm = input("\nDo you want to update now? (Y/n): ").strip().lower()
    
    if confirm == 'n':
        if console:
            console.print("\n[bold]Update cancelled.[/bold]")
        else:
            print("\nUpdate cancelled.")
        return
    
    # Perform update
    if console:
        console.print("\n[bold cyan]Updating...[/bold cyan]")
    else:
        print("\nUpdating...")
    
    try:
        # Pull latest changes
        result = subprocess.run(
            ["git", "-C", str(learn_dir), "pull", "origin", "main"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            if console:
                console.print(f"\n[bold red]Update failed:[/bold red]")
                console.print(f"[dim]{result.stderr}[/dim]")
            else:
                print(f"\nUpdate failed:")
                print(result.stderr)
            return
        
        # Show what was updated
        if console:
            console.print("\n[bold green]✓ Update complete![/bold green]")
            console.print("\n[bold]Changes:[/bold]")
            if result.stdout:
                for line in result.stdout.split('\n')[:10]:  # Show first 10 lines
                    if line.strip():
                        console.print(f"  [dim]{line}[/dim]")
        else:
            print("\n✓ Update complete!")
            print("\nChanges:")
            if result.stdout:
                for line in result.stdout.split('\n')[:10]:
                    if line.strip():
                        print(f"  {line}")
        
        # Reinstall CLI if needed
        if console:
            console.print("\n[bold cyan]Updating CLI...[/bold cyan]")
        else:
            print("\nUpdating CLI...")
        
        cli_install = learn_dir / "CLI" / "install.sh"
        if cli_install.exists():
            subprocess.run(["bash", str(cli_install)], capture_output=True)
        
        if console:
            console.print("\n[bold green]✓ All updates applied successfully![/bold green]")
            console.print("\n[bold yellow]Note:[/bold yellow] You may need to restart the CLI for all changes to take effect.")
        else:
            print("\n✓ All updates applied successfully!")
            print("\nNote: You may need to restart the CLI for all changes to take effect.")
            
    except Exception as e:
        if console:
            console.print(f"\n[bold red]Update error:[/bold red] {str(e)}")
        else:
            print(f"\nUpdate error: {str(e)}")


def reset_user_data(learn_dir: Path):
    """Reset all user data including progress and workspaces"""
    if console:
        console.print("[bold cyan]╔══════════════════════════════════════════════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║              RESET USER DATA                                 ║[/bold cyan]")
        console.print("[bold cyan]╚══════════════════════════════════════════════════════════════╝[/bold cyan]")
        console.print("\n[bold yellow]⚠️  WARNING: This will:[/bold yellow]")
        console.print("  [red]•[/red] Delete all lesson progress")
        console.print("  [red]•[/red] Delete all workspace files (your code)")
        console.print("  [red]•[/red] Delete configuration settings")
        console.print("\n[bold]The LEARN CLI itself will remain installed.[/bold]")
    else:
        print("=" * 70)
        print("  RESET USER DATA")
        print("=" * 70)
        print("\n⚠️  WARNING: This will:")
        print("  • Delete all lesson progress")
        print("  • Delete all workspace files (your code)")
        print("  • Delete configuration settings")
        print("\nThe LEARN CLI itself will remain installed.")

    confirm = input("\nAre you ABSOLUTELY sure? (type 'DELETE' to confirm): ").strip()
    
    if confirm != "DELETE":
        if console:
            console.print("\n[bold green]Reset cancelled.[/bold green]")
        else:
            print("\nReset cancelled.")
        return

    # Get OS type for workspace path
    checker = SystemChecker()
    if checker.os_type == "windows":
        workspace_root = Path.home() / "AppData" / "Local" / "learn" / "workspaces"
    elif checker.os_type == "mac":
        workspace_root = Path.home() / "Library" / "Application Support" / "learn" / "workspaces"
    else:
        workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"

    # Ask about keeping workspaces
    if workspace_root.exists():
        if console:
            console.print("\n[bold cyan]Found workspace directory:[/bold cyan]")
            console.print(f"  {workspace_root}")
        else:
            print(f"\nFound workspace directory:")
            print(f"  {workspace_root}")
        
        keep_workspaces = input("\nDo you want to keep your workspace files? (Y/n): ").strip().lower()
        delete_workspaces = keep_workspaces == 'n'
    else:
        delete_workspaces = False

    # Delete files
    deleted = []
    
    # Progress file
    progress_file = learn_dir / ".learn-progress.json"
    if progress_file.exists():
        progress_file.unlink()
        deleted.append("Progress file")
    
    # Config file
    config_file = learn_dir / ".learn-config.json"
    if config_file.exists():
        config_file.unlink()
        deleted.append("Configuration file")
    
    # Workspaces
    if delete_workspaces and workspace_root.exists():
        shutil.rmtree(workspace_root)
        deleted.append("Workspace directory")
    
    if console:
        console.print("\n[bold green]✓ Data reset complete![/bold green]")
        console.print("\n[bold]Deleted:[/bold]")
        for item in deleted:
            console.print(f"  [green]•[/green] {item}")
        
        if not delete_workspaces and workspace_root.exists():
            console.print(f"\n[bold cyan]Preserved:[/bold cyan]")
            console.print(f"  [cyan]•[/cyan] Workspace files at {workspace_root}")
    else:
        print("\n✓ Data reset complete!")
        print("\nDeleted:")
        for item in deleted:
            print(f"  • {item}")
        
        if not delete_workspaces and workspace_root.exists():
            print(f"\nPreserved:")
            print(f"  • Workspace files at {workspace_root}")


def uninstall_learn(learn_dir: Path):
    """Uninstall LEARN CLI"""
    if console:
        console.print("[bold cyan]╔══════════════════════════════════════════════════════════════╗[/bold cyan]")
        console.print("[bold cyan]║              UNINSTALL LEARN CLI                             ║[/bold cyan]")
        console.print("[bold cyan]╚══════════════════════════════════════════════════════════════╝[/bold cyan]")
        console.print("\n[bold yellow]⚠️  WARNING: This will:[/bold yellow]")
        console.print("  [red]•[/red] Remove the LEARN CLI command")
        console.print("  [red]•[/red] Remove the LEARN repository")
        console.print("  [red]•[/red] Optionally remove user data (progress and workspaces)")
        console.print("\n[dim]Note: This will NOT uninstall Neovim, compilers, or other dependencies[/dim]")
    else:
        print("=" * 70)
        print("  UNINSTALL LEARN CLI")
        print("=" * 70)
        print("\n⚠️  WARNING: This will:")
        print("  • Remove the LEARN CLI command")
        print("  • Remove the LEARN repository")
        print("  • Optionally remove user data (progress and workspaces)")
        print("\nNote: This will NOT uninstall Neovim, compilers, or other dependencies")

    confirm = input("\nAre you sure you want to uninstall? (type 'yes' to confirm): ").strip().lower()
    
    if confirm != "yes":
        if console:
            console.print("\n[bold green]Uninstall cancelled.[/bold green]")
        else:
            print("\nUninstall cancelled.")
        return

    # Ask about user data
    keep_data = input("\nDo you want to keep your user data (progress and workspaces)? (Y/n): ").strip().lower()
    delete_data = keep_data == 'n'

    if console:
        console.print("\n[bold cyan]Uninstalling...[/bold cyan]")
    else:
        print("\nUninstalling...")

    # Get OS type
    checker = SystemChecker()
    
    # Get workspace path
    if checker.os_type == "windows":
        workspace_root = Path.home() / "AppData" / "Local" / "learn" / "workspaces"
    elif checker.os_type == "mac":
        workspace_root = Path.home() / "Library" / "Application Support" / "learn" / "workspaces"
    else:
        workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"

    removed = []
    preserved = []

    # Remove user data if requested
    if delete_data:
        # Progress file
        progress_file = learn_dir / ".learn-progress.json"
        if progress_file.exists():
            progress_file.unlink()
            removed.append("Progress file")
        
        # Config file
        config_file = learn_dir / ".learn-config.json"
        if config_file.exists():
            config_file.unlink()
            removed.append("Configuration file")
        
        # Workspaces
        if workspace_root.exists():
            shutil.rmtree(workspace_root)
            removed.append("Workspace directory")
    else:
        if (learn_dir / ".learn-progress.json").exists():
            preserved.append(f"Progress file at {learn_dir / '.learn-progress.json'}")
        if workspace_root.exists():
            preserved.append(f"Workspaces at {workspace_root}")

    # Remove CLI from PATH (if possible)
    shell_config_updated = False
    if checker.os_type != "windows":
        # Try to remove from shell config
        shell_configs = [
            Path.home() / ".bashrc",
            Path.home() / ".zshrc",
            Path.home() / ".profile",
        ]
        
        for config_file in shell_configs:
            if config_file.exists():
                try:
                    content = config_file.read_text()
                    # Remove LEARN CLI path lines
                    lines = content.split('\n')
                    new_lines = []
                    skip_next = False
                    
                    for line in lines:
                        if '# Learn CLI' in line:
                            skip_next = True
                            continue
                        if skip_next and 'LEARN' in line and 'PATH' in line:
                            skip_next = False
                            continue
                        new_lines.append(line)
                    
                    if len(new_lines) < len(lines):
                        config_file.write_text('\n'.join(new_lines))
                        removed.append(f"PATH entry from {config_file.name}")
                        shell_config_updated = True
                except Exception as e:
                    if console:
                        console.print(f"[yellow]Could not update {config_file.name}: {e}[/yellow]")
    else:
        # Windows - remove from PATH (user PATH variable)
        if console:
            console.print("\n[yellow]Note: You may need to manually remove from PATH on Windows[/yellow]")

    # Show instructions for removing repository
    if console:
        console.print("\n[bold green]✓ Uninstall complete![/bold green]")
        console.print("\n[bold]Removed:[/bold]")
        for item in removed:
            console.print(f"  [green]•[/green] {item}")
        
        if preserved:
            console.print(f"\n[bold cyan]Preserved:[/bold cyan]")
            for item in preserved:
                console.print(f"  [cyan]•[/cyan] {item}")
        
        console.print(f"\n[bold yellow]Final step:[/bold yellow]")
        console.print(f"  To complete uninstallation, manually remove:")
        console.print(f"  [cyan]{learn_dir}[/cyan]")
        console.print(f"\n  Run: [yellow]rm -rf {learn_dir}[/yellow] (Linux/Mac)")
        console.print(f"  Or:  [yellow]Remove-Item -Recurse {learn_dir}[/yellow] (Windows)")
        
        if shell_config_updated:
            console.print(f"\n[bold cyan]Restart your terminal[/bold cyan] for PATH changes to take effect.")
    else:
        print("\n✓ Uninstall complete!")
        print("\nRemoved:")
        for item in removed:
            print(f"  • {item}")
        
        if preserved:
            print(f"\nPreserved:")
            for item in preserved:
                print(f"  • {item}")
        
        print(f"\nFinal step:")
        print(f"  To complete uninstallation, manually remove:")
        print(f"  {learn_dir}")
        print(f"\n  Run: rm -rf {learn_dir} (Linux/Mac)")
        print(f"  Or:  Remove-Item -Recurse {learn_dir} (Windows)")
        
        if shell_config_updated:
            print(f"\nRestart your terminal for PATH changes to take effect.")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Learn Programming - Interactive CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  learn                           # Interactive mode
  learn c++ 1                     # Open C++ Stage 1, Level 1
  learn rust 3 --stage 2          # Open Rust Stage 2, Level 3
  learn --list                    # List all lessons
  learn --progress                # View progress
  learn --next                    # Get next lesson suggestion
  learn --complete c++ 1 1        # Mark C++ Stage 1, Level 1 as complete
        """
    )

    parser.add_argument("language", nargs="?", help="Language (c++, rust, python, js, go, lua)")
    parser.add_argument("level", nargs="?", type=int, help="Level (1-7)")
    parser.add_argument("--stage", type=int, default=1, help="Stage (1-5)")
    parser.add_argument("--vim", action="store_true", help="Open in Vim")
    parser.add_argument("--vscode", action="store_true", help="Open in VS Code")
    parser.add_argument("--terminal", action="store_true", help="Open in terminal")
    parser.add_argument("--list", action="store_true", help="List all lessons")
    parser.add_argument("--progress", action="store_true", help="View progress")
    parser.add_argument("--next", action="store_true", help="Get next lesson")
    parser.add_argument("--complete", nargs=3, metavar=("LANG", "STAGE", "LEVEL"), help="Mark lesson complete")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--init", action="store_true", help="Run first-time setup wizard")
    parser.add_argument("--doctor", action="store_true", help="Check system dependencies")
    parser.add_argument("--run", nargs=3, metavar=("LANG", "STAGE", "LEVEL"), help="Compile and run workspace code")
    parser.add_argument("--reset-data", action="store_true", help="Reset all user data (progress and workspaces)")
    parser.add_argument("--uninstall", action="store_true", help="Uninstall LEARN CLI")
    parser.add_argument("--update", action="store_true", help="Update LEARN to the latest version")
    parser.add_argument("--check-updates", action="store_true", help="Check if updates are available")

    args = parser.parse_args()

    learn_dir = Path(__file__).parent.parent

    # Init wizard
    if args.init:
        wizard = InitWizard(learn_dir)
        wizard.run()
        return

    # Doctor check
    if args.doctor:
        checker = SystemChecker()
        checker.check_all()
        checker.print_report()

        print("Run 'learn init' to install missing components.")
        return

    # Check for updates
    if args.check_updates:
        update_info = check_for_updates(learn_dir)
        
        if "error" in update_info:
            print(f"Error checking for updates: {update_info['error']}")
            return
        
        if console:
            if update_info["has_update"]:
                console.print(f"[bold yellow]Update available![/bold yellow]")
                console.print(f"  Current: [cyan]{update_info['current']}[/cyan]")
                console.print(f"  Latest:  [green]{update_info['latest']}[/green]")
                console.print(f"  Commits behind: [yellow]{update_info['commits_behind']}[/yellow]")
                console.print(f"\nRun [cyan]learn --update[/cyan] to update")
            else:
                console.print(f"[bold green]✓ You're on the latest version[/bold green]")
                console.print(f"[dim]Version: {update_info['current']}[/dim]")
        else:
            if update_info["has_update"]:
                print(f"Update available!")
                print(f"  Current: {update_info['current']}")
                print(f"  Latest:  {update_info['latest']}")
                print(f"  Commits behind: {update_info['commits_behind']}")
                print(f"\nRun 'learn --update' to update")
            else:
                print(f"✓ You're on the latest version")
                print(f"Version: {update_info['current']}")
        return

    # Update
    if args.update:
        update_learn(learn_dir)
        return

    # Reset data
    if args.reset_data:
        reset_user_data(learn_dir)
        return

    # Uninstall
    if args.uninstall:
        uninstall_learn(learn_dir)
        return

    # Run workspace code
    if args.run:
        lang, stage, level = args.run
        lang_map = {
            "c++": "c-c++", "cpp": "c-c++",
            "rust": "rust", "rs": "rust",
            "python": "python", "py": "python",
            "javascript": "javascript", "js": "javascript",
            "go": "go",
            "lua": "lua"
        }
        language = lang_map.get(lang.lower(), lang)

        # Find workspace
        executor = LessonExecutor(None)
        lang_short = executor._get_lang_short_name(language)
        workspace_dir = executor.workspace_root / lang_short / f"stage-{stage}" / f"level-{level}"

        if not workspace_dir.exists():
            print(f"Workspace not found: {workspace_dir}")
            print("Open the lesson first with: learn {lang} {level} --stage {stage}")
            return

        print(f"Running workspace: {workspace_dir}")

        # Run based on language
        if language == "c-c++":
            os.chdir(workspace_dir)
            print("\nCompiling...")
            result = subprocess.run(["make"], capture_output=False)
            if result.returncode == 0:
                print("\nRunning...")
                subprocess.run(["./main"])
        elif language == "rust":
            os.chdir(workspace_dir)
            subprocess.run(["cargo", "run"])
        elif language == "python":
            main_file = workspace_dir / "main.py"
            subprocess.run(["python3", str(main_file)])
        elif language == "javascript":
            main_file = workspace_dir / "main.js"
            subprocess.run(["node", str(main_file)])
        else:
            print(f"Run command not configured for {language}")

        return

    cli = InteractiveCLI(learn_dir)

    # Interactive mode
    if args.interactive or (not args.language and not args.list and not args.progress and not args.next and not args.complete):
        cli.run_interactive_mode()
        return

    # List lessons
    if args.list:
        cli._browse_all_lessons()
        return

    # View progress
    if args.progress:
        cli._view_progress()
        return

    # Next lesson
    if args.next:
        cli._continue_learning()
        return

    # Mark complete
    if args.complete:
        lang, stage, level = args.complete
        lang_map = {
            "c++": "c-c++", "cpp": "c-c++",
            "rust": "rust", "rs": "rust",
            "python": "python", "py": "python",
            "javascript": "javascript", "js": "javascript",
            "go": "go",
            "lua": "lua"
        }
        language = lang_map.get(lang.lower(), lang)
        cli.progress.mark_lesson_completed(language, int(stage), int(level))
        print(f"[OK] Marked {language} Stage {stage} Level {level} as complete!")
        return

    # Open specific lesson
    if args.language and args.level:
        lang_map = {
            "c++": "c-c++", "cpp": "c-c++",
            "rust": "rust", "rs": "rust",
            "python": "python", "py": "python",
            "javascript": "javascript", "js": "javascript",
            "go": "go",
            "lua": "lua"
        }

        language = lang_map.get(args.language.lower(), args.language)

        mode = "vim"
        if args.vscode:
            mode = "vscode"
        elif args.terminal:
            mode = "terminal"

        cli._open_lesson(language, args.stage, args.level, mode)


if __name__ == "__main__":
    main()
