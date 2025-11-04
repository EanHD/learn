#!/usr/bin/env python3
"""
Enhanced Learn CLI - Full-Featured Interactive Learning System
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


class SystemChecker:
    """Checks system dependencies and provides fix commands"""

    def __init__(self):
        self.checks = []

    def check_all(self) -> bool:
        """Run all checks and return True if all pass"""
        self.checks = []

        # Check Neovim
        nvim_ok = self._check_command("nvim", "--version")
        self.checks.append({
            "name": "Neovim",
            "status": "OK" if nvim_ok else "MISSING",
            "fix": "sudo apt install neovim  # or brew install neovim" if not nvim_ok else None,
            "version": self._get_nvim_version() if nvim_ok else None
        })

        # Check compilers
        gcc_ok = self._check_command("gcc", "--version")
        self.checks.append({
            "name": "GCC (C/C++ compiler)",
            "status": "OK" if gcc_ok else "MISSING",
            "fix": "sudo apt install build-essential" if not gcc_ok else None
        })

        clangd_ok = self._check_command("clangd", "--version")
        self.checks.append({
            "name": "clangd (C++ LSP)",
            "status": "OK" if clangd_ok else "MISSING",
            "fix": "sudo apt install clangd" if not clangd_ok else None
        })

        # Check Rust
        rustc_ok = self._check_command("rustc", "--version")
        self.checks.append({
            "name": "Rust compiler",
            "status": "OK" if rustc_ok else "MISSING",
            "fix": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh" if not rustc_ok else None
        })

        # Check Node
        node_ok = self._check_command("node", "--version")
        self.checks.append({
            "name": "Node.js",
            "status": "OK" if node_ok else "MISSING",
            "fix": "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs" if not node_ok else None,
            "version": self._get_command_output("node", "--version") if node_ok else None
        })

        # Check Python
        python_ok = self._check_command("python3", "--version")
        self.checks.append({
            "name": "Python 3",
            "status": "OK" if python_ok else "MISSING",
            "fix": "sudo apt install python3" if not python_ok else None
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
        kickstart_ok = Path.home() / ".config" / "nvim" / "init.lua"
        self.checks.append({
            "name": "Kickstart.nvim config",
            "status": "OK" if kickstart_ok.exists() else "MISSING",
            "fix": "git clone https://github.com/nvim-lua/kickstart.nvim.git ~/.config/nvim" if not kickstart_ok.exists() else None
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

    def _check_mason_packages(self) -> bool:
        """Check if Mason packages are installed"""
        mason_dir = Path.home() / ".local" / "share" / "nvim" / "mason" / "packages"
        if not mason_dir.exists():
            return False

        required = {"clangd", "rust-analyzer", "pyright", "prettierd", "stylua"}
        installed = {p.name for p in mason_dir.iterdir() if p.is_dir()}
        return required.issubset(installed)

    def _get_mason_status(self) -> str:
        """Get Mason package status"""
        mason_dir = Path.home() / ".local" / "share" / "nvim" / "mason" / "packages"
        if not mason_dir.exists():
            return "Mason directory not found"

        installed = sorted([p.name for p in mason_dir.iterdir() if p.is_dir()])
        return f"{len(installed)} packages installed"

    def print_report(self):
        """Print formatted check report"""
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
        self.workspace_root = Path.home() / ".local" / "share" / "learn" / "workspaces"

    def run(self):
        """Run the initialization wizard"""
        self._clear_screen()
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
            os.system('clear' if os.name != 'nt' else 'cls')

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
        print("This may require sudo password.\n")

        for check in self.checker.checks:
            if check["status"] != "OK" and check.get("fix"):
                print(f"Installing {check['name']}...")
                print(f"  Command: {check['fix']}")

                confirm = input("  Run this command? (Y/n): ").strip().lower()
                if confirm != 'n':
                    os.system(check['fix'])

    def _step_editor_selection(self):
        """Select preferred editor"""
        self._clear_screen()
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
        print(f"\n{BG_CYAN}{BOLD} ✨ NEW! QUICK GUIDE POPUP {RESET}")
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
        print(f"{GREEN}💡 Remember: Press {CYAN}{BOLD}<Space>g{RESET}{GREEN} anytime for the complete guide!{RESET}")
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
                    print("\n👋 Tutorial ended. You can restart anytime with option 8!")
                    input("Press Enter to return to main menu...")
                    return

            self.current_step += 1

    def _clear_screen(self):
        if utils:
            utils.clear_screen()
        else:
            os.system('clear' if os.name != 'nt' else 'cls')

    def _intro(self):
        print("=" * 70)
        print("  📚 WELCOME TO THE LEARN CLI INTERACTIVE TUTORIAL")
        print("=" * 70)
        print("\nThis tutorial will teach you how to use the Learn CLI effectively.")
        print("\n🎯 What you'll learn:")
        print("  • How to navigate the CLI")
        print("  • Understanding lesson structure")
        print("  • Using Vim mode efficiently")
        print("  • Tracking your progress")
        print("  • Advanced features and tips")
        print("\n⏱️  Estimated time: 5 minutes")

    def _navigation_basics(self):
        print("=" * 70)
        print("  STEP 1: NAVIGATION BASICS")
        print("=" * 70)
        print("\n📖 The Main Menu:")
        print("\nWhen you run 'learn', you see the main menu with these options:\n")
        print("  1. Start a lesson     → Begin learning a specific lesson")
        print("  2. Continue           → Pick up where you left off")
        print("  3. View progress      → See your completion status")
        print("  4. Browse all         → Explore all available lessons")
        print("  5. Switch language    → Change programming language")
        print("  6. Mark complete      → Flag a lesson as done")
        print("  7. Statistics         → View detailed stats")
        print("  8. Tutorial           → You're here now!")
        print("\n💡 TIP: You can also use command-line arguments:")
        print("  learn c++ 1           → Directly open C++ Stage 1, Level 1")
        print("  learn --list          → List all lessons")
        print("  learn --next          → Get next lesson suggestion")

    def _lesson_structure(self):
        print("=" * 70)
        print("  STEP 2: LESSON STRUCTURE")
        print("=" * 70)
        print("\n📚 How Lessons Are Organized:\n")
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
        print("\n📝 Each stage has 7 LEVELS (lessons) to complete.")

    def _vim_mode_tutorial(self):
        print("=" * 70)
        print("  STEP 3: VIM MODE (DEFAULT)")
        print("=" * 70)
        print("\n🚀 When you open a lesson, you'll see a SPLIT-SCREEN view:\n")
        print("  ┌──────────────────┬──────────────────┐")
        print("  │                  │                  │")
        print("  │  LESSON TEXT     │  YOUR CODE       │")
        print("  │  (Read-only)     │  (Editable)      │")
        print("  │                  │                  │")
        print("  └──────────────────┴──────────────────┘")
        print("\n⌨️  Essential Vim Commands:\n")
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
        print("\n💡 TIP: Your LazyVim config is active, so you have:")
        print("  • LSP autocomplete (clangd, rust-analyzer, etc.)")
        print("  • Auto-formatting on save")
        print("  • Syntax highlighting")
        print("  • All your custom keybindings")

    def _progress_tracking(self):
        print("=" * 70)
        print("  STEP 4: PROGRESS TRACKING")
        print("=" * 70)
        print("\n📊 Your progress is automatically tracked!\n")
        print("  • Every lesson you open is recorded")
        print("  • You can mark lessons as 'completed'")
        print("  • View stats anytime with option 3 or 7")
        print("\n✅ Marking Lessons Complete:\n")
        print("  From the main menu:")
        print("    → Select option 6 (Mark lesson as complete)")
        print("    → Enter: language, stage, level")
        print("\n  From command line:")
        print("    learn --complete c++ 1 1")
        print("\n📈 Progress is saved in: .learn-progress.json")
        print("\n💡 TIP: Use 'learn --next' to get a suggestion for")
        print("         what to study next based on your progress!")

    def _advanced_features(self):
        print("=" * 70)
        print("  STEP 5: ADVANCED FEATURES")
        print("=" * 70)
        print("\n🔧 Power User Tips:\n")
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
        print("\n💡 SETUP COMPLETE:")
        print("  • Full LSP support (autocomplete, diagnostics)")
        print("  • Auto-formatting on save")
        print("  • 9 formatters & LSPs installed via Mason")

    def _completion(self):
        print("=" * 70)
        print("  🎉 TUTORIAL COMPLETE!")
        print("=" * 70)
        print("\n✨ You're now ready to start learning!\n")
        print("📚 Quick Reference Card:\n")
        print("  Start learning:     learn c++ 1")
        print("  Continue:           learn --next")
        print("  List lessons:       learn --list")
        print("  Check progress:     learn --progress")
        print("  Get help:           learn --help")
        print("\n🚀 Recommended First Steps:")
        print("  1. Run: learn c++ 1")
        print("  2. Practice Vim navigation (Ctrl-h/l)")
        print("  3. Complete the lesson")
        print("  4. Mark it complete: learn --complete c++ 1 1")
        print("  5. Continue to next lesson: learn --next")
        print("\n💪 Happy Learning!")
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
            self._print_main_menu()

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
            elif choice == "q" or choice == "0":
                print("\n👋 Happy learning!")
                break
            else:
                print("Invalid option. Press Enter to continue...")
                input()

    def _clear_screen(self):
        """Clear terminal screen"""
        if utils:
            utils.clear_screen()
        else:
            os.system('clear' if os.name != 'nt' else 'cls')

    def _print_header(self):
        """Print CLI header"""
        print("=" * 70)
        print("  📚 LEARN CLI - Interactive Programming Learning System")
        print("=" * 70)

    def _print_main_menu(self):
        """Print main menu"""
        print("\n🎯 MAIN MENU\n")
        print("  1. Start a lesson")
        print("  2. Continue where you left off")
        print("  3. View progress")
        print("  4. Browse all lessons")
        print("  5. Switch language")
        print("  6. Mark lesson as complete")
        print("  7. View statistics")
        print("  8. 📚 Interactive Tutorial (New!)")
        print("  0. Exit")

    def _select_language_and_lesson(self):
        """Select language and lesson interactively"""
        self._clear_screen()
        print("📝 SELECT LANGUAGE\n")

        languages = list(self.lesson_mgr.languages.keys())
        for idx, lang in enumerate(languages, 1):
            display_name = self.lesson_mgr.get_language_display_name(lang)
            print(f"  {idx}. {display_name}")

        lang_choice = input("\n→ Select language (or 'b' to go back): ").strip()

        if lang_choice.lower() == 'b':
            return

        try:
            lang_idx = int(lang_choice) - 1
            if 0 <= lang_idx < len(languages):
                language = languages[lang_idx]
                self._select_stage_and_level(language)
        except ValueError:
            print("Invalid choice!")
            input("Press Enter to continue...")

    def _select_stage_and_level(self, language: str):
        """Select stage and level"""
        self._clear_screen()
        display_name = self.lesson_mgr.get_language_display_name(language)
        print(f"📖 {display_name.upper()} - SELECT LESSON\n")

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
            print(f"\n❌ Lesson not found: Stage {stage}, Level {level}")
            input("Press Enter to continue...")
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
        print("\n🎨 SELECT MODE\n")
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
            print("\n📚 No previous sessions found. Start with a new lesson!")
            input("Press Enter to continue...")
            return

        last_session = sessions[-1]
        language = last_session["language"]

        next_lesson = self.progress.get_next_lesson(language)

        if next_lesson:
            stage, level = next_lesson
            display_name = self.lesson_mgr.get_language_display_name(language)

            print(f"\n✨ Next lesson: {display_name} - Stage {stage}, Level {level}")
            confirm = input("→ Open this lesson? (Y/n): ").strip().lower()

            if confirm != 'n':
                self._open_lesson(language, stage, level)
        else:
            print(f"\n🎉 Congratulations! You've completed all lessons in {language}!")
            input("Press Enter to continue...")

    def _view_progress(self):
        """View learning progress"""
        self._clear_screen()
        print("📊 YOUR LEARNING PROGRESS\n")

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
            print(f"\n📈 Total sessions: {len(sessions)}")

            last_session = sessions[-1]
            lang_display = self.lesson_mgr.get_language_display_name(last_session["language"])
            print(f"💡 Last session: {lang_display} - Stage {last_session['stage']}, Level {last_session['level']}")

        input("\nPress Enter to continue...")

    def _browse_all_lessons(self):
        """Browse all available lessons"""
        self._clear_screen()
        print("📚 ALL AVAILABLE LESSONS\n")

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
        print("✅ MARK LESSON AS COMPLETE\n")

        languages = list(self.lesson_mgr.languages.keys())
        for idx, lang in enumerate(languages, 1):
            display_name = self.lesson_mgr.get_language_display_name(lang)
            print(f"  {idx}. {display_name}")

        lang_choice = input("\n→ Select language: ").strip()

        try:
            lang_idx = int(lang_choice) - 1
            if 0 <= lang_idx < len(languages):
                language = languages[lang_idx]

                stage = int(input("→ Stage number (1-5): ").strip())
                level = int(input("→ Level number (1-7): ").strip())

                if self.progress.mark_lesson_completed(language, stage, level):
                    print(f"\n✨ Lesson marked as complete!")
                else:
                    print(f"\n❌ Lesson not found in progress.")
        except ValueError:
            print("Invalid input!")

        input("Press Enter to continue...")

    def _view_stats(self):
        """View detailed statistics"""
        self._clear_screen()
        print("📊 DETAILED STATISTICS\n")

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
        print(f"✅ Marked {language} Stage {stage} Level {level} as complete!")
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
