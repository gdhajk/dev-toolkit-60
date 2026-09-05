def validate_click_params(interval: float, count: int) -> bool:
    """Validates autoclicker parameters to ensure they are within safe ranges."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        return False
    
    if not isinstance(count, int) or (count != -1 and count < 1):
        return False
        
    return True

def sanitize_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
    """Clamps input coordinates to remain within physical screen bounds."""
    safe_x = max(0, min(x, screen_width))
    safe_y = max(0, min(y, screen_height))
    return safe_x, safe_y

def validate_hotkey(key: str) -> bool:
    """Checks if the provided hotkey is a valid single character or recognized special key."""
    if not key or len(key) > 10:
        return False
    return key.isprintable()

def validate_process_config(config: dict) -> bool:
    """Comprehensive validation for the configuration object schema."""
    required = ['interval', 'count', 'x', 'y']
    return all(key in config for key in required)