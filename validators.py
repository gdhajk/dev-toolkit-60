from typing import Dict, Any

class ValidationError(Exception):
    pass

def validate_click_config(config: Dict[str, Any]) -> bool:
    """
    Validate autoclicker configuration parameters before processing.
    Ensures interval, clicks, and button types are within safe operational bounds.
    """
    interval = config.get("interval")
    if interval is None or not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValidationError("Interval must be a float or int >= 0.01 seconds.")

    clicks = config.get("clicks")
    if clicks is not None and (not isinstance(clicks, int) or clicks < -1):
        raise ValidationError("Clicks must be -1 (infinite) or a positive integer.")

    button = config.get("button")
    valid_buttons = {"left", "right", "middle"}
    if button not in valid_buttons:
        raise ValidationError(f"Button must be one of {valid_buttons}.")

    return True

def sanitize_coordinates(x: Any, y: Any) -> tuple[int, int]:
    """
    Sanitize and cast screen coordinates to integers.
    Raises ValidationError if coordinates are out of bounds or invalid types.
    """
    try:
        coord_x = int(x)
        coord_y = int(y)
    except (TypeError, ValueError) as exc:
        raise ValidationError("Coordinates must be valid integers.") from exc

    if coord_x < 0 or coord_y < 0:
        raise ValidationError("Coordinates cannot be negative.")

    return coord_x, coord_y
