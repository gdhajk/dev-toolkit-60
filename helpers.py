import json
from typing import List, Dict, Any, Optional


def validate_click_data(data: Dict[str, Any]) -> bool:
    """Check if the provided data has valid structure for clicks."""
    if not isinstance(data, dict):
        return False
    if 'clicks' not in data or 'interval' not in data:
        return False
    clicks = data['clicks']
    if not isinstance(clicks, list) or len(clicks) == 0:
        return False
    for click in clicks:
        if not isinstance(click, dict):
            return False
        if 'x' not in click or 'y' not in click:
            return False
        try:
            float(click['x'])
            float(click['y'])
        except (ValueError, TypeError):
            return False
    interval = data['interval']
    if not isinstance(interval, (int, float)) or interval <= 0:
        return False
    return True


def process_click_data(raw_clicks: List[Dict[str, Any]], default_interval: float = 0.1) -> Dict[str, Any]:
    """Convert raw list of clicks into structured data dict."""
    if not raw_clicks:
        return {'clicks': [], 'interval': default_interval}
    processed_clicks = []
    for idx, click in enumerate(raw_clicks):
        x = click.get('x', 0)
        y = click.get('y', 0)
        delay = click.get('delay', default_interval)
        processed_clicks.append({
            'x': float(x),
            'y': float(y),
            'delay': float(delay),
            'order': idx + 1
        })
    return {
        'clicks': processed_clicks,
        'interval': default_interval,
        'count': len(processed_clicks)
    }


def save_to_file(data: Dict[str, Any], path: str) -> bool:
    """Persist click data to a JSON file if valid."""
    if not validate_click_data(data):
        return False
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except (IOError, OSError, TypeError):
        return False


def load_from_file(path: str) -> Optional[Dict[str, Any]]:
    """Retrieve click data from JSON file and validate it."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if validate_click_data(data):
            return data
        return None
    except (IOError, OSError, json.JSONDecodeError, TypeError):
        return None


def get_click_summary(data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate summary statistics from valid click data."""
    if not validate_click_data(data):
        return {'valid': False}
    clicks = data['clicks']
    xs = [c['x'] for c in clicks]
    ys = [c['y'] for c in clicks]
    summary = {
        'valid': True,
        'click_count': len(clicks),
        'interval': data['interval'],
        'x_range': (min(xs), max(xs)),
        'y_range': (min(ys), max(ys)),
        'center': (sum(xs)/len(xs), sum(ys)/len(ys))
    }
    return summary
