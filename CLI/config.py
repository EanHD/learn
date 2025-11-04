"""
Configuration management for Learn CLI.
Handles user preferences, defaults, and persistence.
"""

import json
import os
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional

try:
    from . import utils
except ImportError:
    import utils


@dataclass
class Config:
    """User configuration"""
    default_editor: str = "vim"  # vim, vscode, terminal
    default_language: Optional[str] = None
    workspace_dir: Optional[str] = None
    nvim_config: Optional[str] = None
    progress_file: Optional[str] = None
    auto_save_progress: bool = True
    show_welcome: bool = True
    color_output: bool = True
    # cli_mode removed - unified CLI now

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Config':
        """Create from dictionary - ignores old cli_mode for graceful migration"""
        # Filter out cli_mode if it exists (legacy config files)
        filtered = {k: v for k, v in data.items() if k in cls.__annotations__}
        return cls(**filtered)


class ConfigManager:
    """Manages user configuration"""

    def __init__(self, config_file: Optional[str] = None):
        if config_file:
            self.config_file = Path(config_file)
        else:
            config_dir = utils.get_config_dir()
            utils.ensure_dir(config_dir)
            self.config_file = Path(config_dir) / "config.json"

        self.config = self.load()

    def load(self) -> Config:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    return Config.from_dict(data)
            except Exception as e:
                print(f"Warning: Could not load config: {e}")
                return Config()
        return Config()

    def save(self) -> bool:
        """Save configuration to file"""
        try:
            utils.ensure_dir(str(self.config_file.parent))
            content = json.dumps(self.config.to_dict(), indent=2)
            return utils.atomic_write(str(self.config_file), content)
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Get config value"""
        return getattr(self.config, key, default)

    def set(self, key: str, value: Any) -> bool:
        """Set config value"""
        if hasattr(self.config, key):
            setattr(self.config, key, value)
            return self.save()
        return False

    def get_workspace_dir(self) -> Path:
        """Get workspace directory"""
        if self.config.workspace_dir:
            return Path(self.config.workspace_dir)
        return Path.home() / ".local" / "share" / "learn" / "workspaces"

    def get_progress_file(self) -> Path:
        """Get progress file path"""
        if self.config.progress_file:
            return Path(self.config.progress_file)
        config_dir = Path(utils.get_config_dir())
        return config_dir / "progress.json"

    def get_nvim_config(self) -> Optional[Path]:
        """Get custom Neovim config path"""
        if self.config.nvim_config:
            return Path(self.config.nvim_config)
        return None

    def reset(self) -> bool:
        """Reset to default configuration"""
        self.config = Config()
        return self.save()


# Global config instance (lazy loaded)
_config_manager: Optional[ConfigManager] = None


def get_config() -> ConfigManager:
    """Get global config manager instance"""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager
