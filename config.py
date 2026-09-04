import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_data = json.load(f)
                config.update(user_data)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass

if __name__ == "__main__":
    # Example usage for dev-toolkit-60
    current_cfg = load_config()
    print(f"Active configuration: {current_cfg}")