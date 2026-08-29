"""
Constants for autoclicker error handling in dev-toolkit-60.
"""

import sys
from typing import Dict, Optional

# Autoclicker parameter constants
DEFAULT_INTERVAL = 0.05
MIN_INTERVAL = 0.001
MAX_INTERVAL = 10.0
MAX_CLICKS = 100000

# Screen bounds constants
MIN_X = 0
MIN_Y = 0
MAX_X = 2560
MAX_Y = 1440

# Error codes for edge cases
ERR_INVALID_INTERVAL = 1
ERR_OUT_OF_BOUNDS = 2
ERR_PERMISSION = 3
ERR_CLICK_FAIL = 4
ERR_UNKNOWN = 0

# Error messages
ERROR_MESSAGES: Dict[int, str] = {
    ERR_INVALID_INTERVAL: "Interval must be between {min} and {max} seconds",
    ERR_OUT_OF_BOUNDS: "Position out of bounds: ({x}, {y}) not in ({minx}-{maxx}, {miny}-{maxy})",
    ERR_PERMISSION: "Permission denied for autoclick actions",
    ERR_CLICK_FAIL: "Click operation failed",
    ERR_UNKNOWN: "Unknown autoclick error",
}

# Error recovery constants
MAX_RETRIES = 3
RETRY_DELAY = 0.5

def validate_params(interval: float, x: int, y: int) -> Optional[int]:
    """Return error code for invalid params or None."""
    if interval < MIN_INTERVAL or interval > MAX_INTERVAL:
        return ERR_INVALID_INTERVAL
    if x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y:
        return ERR_OUT_OF_BOUNDS
    return None

def format_error(code: int, **kwargs) -> str:
    """Format error message, handle missing keys."""
    template = ERROR_MESSAGES.get(code, ERROR_MESSAGES[ERR_UNKNOWN])
    try:
        return template.format(**kwargs)
    except (KeyError, ValueError):
        return template

def handle_error(code: int, **context) -> None:
    """Print error and exit for critical cases."""
    msg = format_error(code, **context)
    print(f"Error {code}: {msg}")
    if code == ERR_PERMISSION:
        print("Exiting due to permission issue.")
        sys.exit(1)

# Additional constants
CLICK_MODIFIERS = ["ctrl", "shift"]
LOG_LEVELS = {"DEBUG": 10, "INFO": 20, "ERROR": 40}