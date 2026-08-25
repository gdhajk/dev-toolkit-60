import json
import os
from typing import Dict, Any

# Default configuration for the autoclicker
DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 100,  # milliseconds between clicks
    "hotkey": "f8",  # key to toggle clicking
    "max_clicks": 0,  # 0 for unlimited clicks
    "target_window": "",  # empty for any window
    "randomize": False,  # add randomness to interval
    "random_range": 50  # max variation in ms
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file, falling back to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
            # Merge user config into defaults
            for key, value in user_config.items():
                if key in config:
                    config[key] = value
        except (json.JSONDecodeError, IOError, OSError) as e:
            # Fall back to defaults on error
            print(f"Config load error, using defaults: {e}")
    
    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> bool:
    """Save the configuration to a JSON file."""
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        return True
    except (IOError, OSError) as e:
        print(f"Failed to save config: {e}")
        return False

def get_default_config() -> Dict[str, Any]:
    """Return a copy of the default configuration dictionary."""
    return DEFAULT_CONFIG.copy()

def validate_and_load(config_path: str = "config.json") -> Dict[str, Any]:
    """Load config with defaults and basic validation."""
    config = load_config(config_path)
    
    # Basic validation
    if config["click_interval"] < 1:
        config["click_interval"] = DEFAULT_CONFIG["click_interval"]
    if not isinstance(config["hotkey"], str):
        config["hotkey"] = DEFAULT_CONFIG["hotkey"]
    if config["max_clicks"] < 0:
        config["max_clicks"] = 0
    
    return config

# Example usage
if __name__ == "__main__":
    cfg = validate_and_load()
    print("Loaded config:", cfg)