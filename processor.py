import time

def validate_click_data(click_data):
    if not isinstance(click_data, dict):
        return False
    required = ['x', 'y', 'delay']
    if not all(key in click_data for key in required):
        return False
    try:
        x = int(click_data['x'])
        y = int(click_data['y'])
        delay = float(click_data['delay'])
        if not (0 <= x <= 1920 and 0 <= y <= 1080):
            return False
        if not (0.05 <= delay <= 5.0):
            return False
        return True
    except (ValueError, TypeError):
        return False

def main_processing_loop(click_sequence):
    if not isinstance(click_sequence, list):
        print("Invalid sequence: must be list")
        return
    valid_clicks = 0
    for i, click_data in enumerate(click_sequence):
        if not validate_click_data(click_data):
            print(f"Invalid click data at index {i}, skipping")
            continue
        x = int(click_data['x'])
        y = int(click_data['y'])
        delay = float(click_data['delay'])
        print(f"Processing click {i+1} at ({x}, {y}) with delay {delay}s")
        time.sleep(delay)
        valid_clicks += 1
    print(f"Completed {valid_clicks} valid clicks")

if __name__ == "__main__":
    sample_sequence = [
        {"x": 100, "y": 200, "delay": 0.5},
        {"x": "abc", "y": 300, "delay": 1.0},
        {"x": 500, "y": 600, "delay": 0.2},
        {"x": 3000, "y": 400, "delay": 0.5},
    ]
    main_processing_loop(sample_sequence)