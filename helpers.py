import time
import random

def click(x, y):
    """Simulates a mouse click at the specified (x, y) coordinates."""
    import pyautogui
    pyautogui.click(x, y)


def perform_clicks(num_clicks, delay=0):
    """Performs multiple clicks with an optional delay between them."""
    for _ in range(num_clicks):
        x = random.randint(0, 1920)  # Screen width
        y = random.randint(0, 1080)  # Screen height
        click(x, y)
        time.sleep(delay)


def wait_for(seconds):
    """Pauses execution for a specified number of seconds."""
    time.sleep(seconds)


def random_delay(min_delay, max_delay):
    """Returns a random delay between the specified min and max values."""
    return random.uniform(min_delay, max_delay)


def validate_coordinates(x, y):
    """Ensures the provided coordinates are within screen bounds."""
    return 0 <= x <= 1920 and 0 <= y <= 1080
