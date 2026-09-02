import time
import random

# Autoclicker helper functions with robust error handling for edge cases

def validate_click_parameters(clicks, interval, x, y):
    if not isinstance(clicks, int):
        raise ValueError("Clicks must be an integer")
    if clicks <= 0:
        raise ValueError("Clicks must be greater than zero")
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError("Interval must be a positive number")
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Coordinates must be integers")
    if x < 0 or y < 0:
        raise ValueError("Coordinates must not be negative")
    if interval < 0.01:
        raise ValueError("Interval too small, potential performance issues")
    if clicks > 100000:
        print("Warning: High click count specified")

def perform_single_click(x, y):
    try:
        print(f"Clicking at ({x}, {y})")
        time.sleep(random.uniform(0.01, 0.05))
        return True
    except Exception as e:
        print(f"Click error: {e}")
        return False

def run_autoclicker(clicks, interval, x, y):
    try:
        # Check for invalid parameters and other edge cases before starting
        validate_click_parameters(clicks, interval, x, y)
        print(f"Starting {clicks} clicks every {interval} seconds")
        for i in range(clicks):
            if not perform_single_click(x, y):
                print("Stopping after click failure")
                break
            time.sleep(interval)
        print("Autoclicker run completed")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("Stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
        reset_on_error()

def reset_on_error():
    print("Resetting after error")
    time.sleep(0.5)

def log_error(error_msg):
    print(f"Logged error: {error_msg}")