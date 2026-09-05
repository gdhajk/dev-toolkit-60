import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": 0
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            # Merge with defaults to ensure missing keys are filled
            config = DEFAULT_CONFIG.copy()
            config.update(data)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> bool:
    """Persists current configuration to json file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False