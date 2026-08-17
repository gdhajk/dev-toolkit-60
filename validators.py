import re

class ValidationError(Exception):
    pass

def validate_click_coordinates(coordinates):
    if not isinstance(coordinates, tuple):
        raise ValidationError('Coordinates must be a tuple.')
    if len(coordinates) != 2:
        raise ValidationError('Coordinates must contain exactly two values.')
    x, y = coordinates
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError('Coordinates must be integers.')
    if not (0 <= x <= 1920 and 0 <= y <= 1080):
        raise ValidationError('Coordinates must be within screen resolution bounds.')

def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise ValidationError('Interval must be a number.')
    if interval <= 0:
        raise ValidationError('Interval must be positive.')

def validate_clicks_count(count):
    if not isinstance(count, int):
        raise ValidationError('Count must be an integer.')
    if count <= 0:
        raise ValidationError('Count must be positive.')

def validate_hotkey(hotkey):
    if not isinstance(hotkey, str):
        raise ValidationError('Hotkey must be a string.')
    if not re.match(r'^[a-zA-Z]+$', hotkey):
        raise ValidationError('Hotkey must contain only letters.')
