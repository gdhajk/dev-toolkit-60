import json
from typing import Any, Dict

class InvalidDataError(Exception):
    pass

def validate_autoclicker_data(data: Dict[str, Any]) -> bool:
    required_keys = ['click_interval', 'duration', 'clicks']
    for key in required_keys:
        if key not in data:
            raise InvalidDataError(f'Missing required key: {key}')
        if not isinstance(data[key], (int, float)):
            raise InvalidDataError(f'Invalid type for key {key}: {type(data[key])}')

    if data['click_interval'] <= 0:
        raise InvalidDataError('Click interval must be positive')
    if data['duration'] <= 0:
        raise InvalidDataError('Duration must be positive')
    if data['clicks'] <= 0:
        raise InvalidDataError('Clicks must be positive')

    return True

def load_autoclicker_config(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    validate_autoclicker_data(data)
    return data

