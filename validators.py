def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise ValueError("Click interval must be a number.")
    if interval <= 0:
        raise ValueError("Click interval must be greater than zero.")
    return True


def validate_click_count(count):
    if not isinstance(count, int):
        raise ValueError("Click count must be an integer.")
    if count <= 0:
        raise ValueError("Click count must be greater than zero.")
    return True


def validate_hotkey(hotkey):
    if not isinstance(hotkey, str) or len(hotkey) == 0:
        raise ValueError("Hotkey must be a non-empty string.")
    return True


# Example usage in a main processing loop:
if __name__ == "__main__":
    try:
        click_interval = 0.1  # Example interval
        click_count = 10  # Example count
        hotkey = 'ctrl+c'  # Example hotkey
        
        validate_click_interval(click_interval)
        validate_click_count(click_count)
        validate_hotkey(hotkey)

        print("All inputs are valid.")
    except ValueError as e:
        print(f"Input validation error: {e}")