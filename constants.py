import json
from enum import Enum
from typing import Dict, Any

class MouseButton(Enum):
    """Mouse buttons for clicking."""
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"

class ClickMode(Enum):
    """Modes for autoclicker operation."""
    SINGLE = "single"
    DOUBLE = "double"
    BURST = "burst"
    HOLD = "hold"

# Default timing constants in milliseconds
DEFAULT_INTERVAL = 100
MIN_INTERVAL = 10
MAX_INTERVAL = 10000

DEFAULT_RANDOM_MIN = 50
DEFAULT_RANDOM_MAX = 200

# Hotkey constants
START_HOTKEY = "f6"
STOP_HOTKEY = "f7"
PAUSE_HOTKEY = "f8"
EXIT_HOTKEY = "esc"

# Application constants
APP_NAME = "dev-toolkit-60"
VERSION = "0.6.0"
CONFIG_FILE = "autoclicker_config.json"
LOG_FILE = "autoclicker.log"

# Default configuration dictionary
DEFAULT_CONFIG: Dict[str, Any] = {
    "interval": DEFAULT_INTERVAL,
    "button": MouseButton.LEFT.value,
    "mode": ClickMode.SINGLE.value,
    "randomize": False,
    "random_min": DEFAULT_RANDOM_MIN,
    "random_max": DEFAULT_RANDOM_MAX,
    "start_hotkey": START_HOTKEY,
    "stop_hotkey": STOP_HOTKEY,
    "pause_hotkey": PAUSE_HOTKEY,
    "exit_hotkey": EXIT_HOTKEY,
    "click_count": 0,
    "burst_count": 5,
    "burst_delay": 500
}

def get_default_config() -> Dict[str, Any]:
    """Return a copy of the default configuration."""
    return DEFAULT_CONFIG.copy()

def load_config(file_path: str = CONFIG_FILE) -> Dict[str, Any]:
    """Load config from file or return defaults."""
    try:
        with open(file_path, "r") as file:
            config = json.load(file)
            if not isinstance(config, dict):
                return get_default_config()
            return config

    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return get_default_config()

def save_config(config: Dict[str, Any], file_path: str = CONFIG_FILE) -> bool:
    """Save config to JSON file."""
    try:
        with open(file_path, "w") as file:
            json.dump(config, file, indent=2)
        return True

    except (IOError, PermissionError):
        return False
