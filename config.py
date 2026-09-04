from typing import Dict, Any, Optional
import json
import os

class ConfigManager:
    """Handles loading and persistence of application settings."""

    def __init__(self, config_path: str = "settings.json") -> None:
        self.config_path: str = config_path
        self.settings: Dict[str, Any] = {
            "interval": 0.1,
            "button": "left",
            "hotkey": "f6"
        }

    def load(self) -> None:
        """Reads configuration from a local JSON file."""
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                self.settings.update(json.load(f))

    def save(self) -> None:
        """Writes current settings to a JSON file."""
        with open(self.config_path, "w") as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a specific configuration value."""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Updates a specific configuration value."""
        self.settings[key] = value