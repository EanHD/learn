"""
Cross-platform utilities for the Learn CLI.
"""

import os
import sys
import platform
import subprocess
from typing import Optional


def get_platform() -> str:
    """Get platform identifier (linux, mac, windows)"""
    system = platform.system().lower()
    if system == "darwin":
        return "mac"
    elif system in ["linux", "windows"]:
        return system
    return "linux"  # default fallback


def clear_screen():
    """Clear the terminal screen (cross-platform)"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def show_pager(content: str):
    """Show content in a pager (cross-platform)"""
    try:
        import pydoc
        pydoc.pager(content)
    except Exception:
        # Fallback to print if pager fails
        print(content)


def open_editor(file_path: str, editor: str = "vim") -> bool:
    """Open file in editor (cross-platform)"""
    try:
        if editor == "vim" or editor == "nvim":
            # Use nvim if available, otherwise fall back to vim
            cmd = "nvim" if which("nvim") else "vim"
            subprocess.run([cmd, file_path])
        elif editor == "vscode" or editor == "code":
            subprocess.run(["code", file_path])
        else:
            # Try default editor
            if platform.system() == "Windows":
                os.startfile(file_path)
            elif platform.system() == "Darwin":
                subprocess.run(["open", file_path])
            else:
                subprocess.run(["xdg-open", file_path])
        return True
    except Exception as e:
        print(f"Error opening editor: {e}")
        return False


def which(cmd: str) -> Optional[str]:
    """Cross-platform which command"""
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["where", cmd],
                capture_output=True,
                text=True,
                check=False
            )
        else:
            result = subprocess.run(
                ["which", cmd],
                capture_output=True,
                text=True,
                check=False
            )

        if result.returncode == 0:
            return result.stdout.strip().split('\n')[0]
        return None
    except Exception:
        return None


def check_command(cmd: str, *args) -> bool:
    """Check if a command exists and runs (cross-platform)"""
    try:
        subprocess.run(
            [cmd, *args],
            capture_output=True,
            check=False,
            timeout=2
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        return False


def get_command_output(cmd: str, *args) -> Optional[str]:
    """Get output from a command"""
    try:
        result = subprocess.run(
            [cmd, *args],
            capture_output=True,
            text=True,
            check=False,
            timeout=2
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except Exception:
        return None


def get_home_dir() -> str:
    """Get user home directory (cross-platform)"""
    return str(os.path.expanduser("~"))


def get_config_dir() -> str:
    """Get config directory (cross-platform, follows OS conventions)"""
    system = platform.system()

    if system == "Windows":
        # Windows: %APPDATA%\learn
        return os.path.join(os.environ.get("APPDATA", get_home_dir()), "learn")
    elif system == "Darwin":
        # macOS: ~/Library/Application Support/learn
        return os.path.join(get_home_dir(), "Library", "Application Support", "learn")
    else:
        # Linux/Unix: ~/.config/learn (XDG Base Directory)
        xdg_config = os.environ.get("XDG_CONFIG_HOME")
        if xdg_config:
            return os.path.join(xdg_config, "learn")
        return os.path.join(get_home_dir(), ".config", "learn")


def ensure_dir(path: str):
    """Ensure directory exists"""
    os.makedirs(path, exist_ok=True)


def atomic_write(file_path: str, content: str, retries: int = 3):
    """Write file atomically with retries"""
    import tempfile
    import shutil

    for attempt in range(retries):
        try:
            # Write to temp file
            dir_path = os.path.dirname(file_path) or "."
            with tempfile.NamedTemporaryFile(
                mode='w',
                dir=dir_path,
                delete=False,
                suffix='.tmp'
            ) as tmp:
                tmp.write(content)
                tmp_path = tmp.name

            # Move temp file to target (atomic on POSIX)
            shutil.move(tmp_path, file_path)
            return True

        except Exception as e:
            if attempt == retries - 1:
                print(f"Error writing file after {retries} attempts: {e}")
                return False
            continue

    return False


def get_terminal_size() -> tuple:
    """Get terminal size (width, height)"""
    try:
        size = os.get_terminal_size()
        return (size.columns, size.lines)
    except Exception:
        return (80, 24)  # default fallback


def is_windows() -> bool:
    """Check if running on Windows"""
    return platform.system() == "Windows"


def is_mac() -> bool:
    """Check if running on macOS"""
    return platform.system() == "Darwin"


def is_linux() -> bool:
    """Check if running on Linux"""
    return platform.system() == "Linux"
