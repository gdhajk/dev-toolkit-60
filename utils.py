import time
import random
import threading
from typing import Tuple, Optional

class ClickUtils:
    """Utility class for autoclicker click operations."""

    def __init__(self, min_delay: float = 0.05, max_delay: float = 0.3, jitter: int = 3):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.jitter = jitter

    def get_delay(self) -> float:
        """Generate randomized delay for clicks."""
        return random.uniform(self.min_delay, self.max_delay)

    def apply_jitter(self, x: int, y: int) -> Tuple[int, int]:
        """Apply random jitter to click position."""
        jitter_x = x + random.randint(-self.jitter, self.jitter)
        jitter_y = y + random.randint(-self.jitter, self.jitter)
        return jitter_x, jitter_y

    def click_sequence(self, num_clicks: int, x: int, y: int, interval: float) -> None:
        """Perform a sequence of clicks with jitter and delays."""
        for i in range(num_clicks):
            pos_x, pos_y = self.apply_jitter(x, y)
            # Simulate click action for demo
            print(f"Performing click {i+1} at position ({pos_x}, {pos_y})")
            time.sleep(self.get_delay())
            time.sleep(random.uniform(interval * 0.5, interval * 1.5))

    def run_autoclick(self, x: int, y: int, clicks_per_cycle: int = 5, cycle_interval: float = 1.0, stop_event: Optional[threading.Event] = None) -> None:
        """Run autoclicker in loop with stop support."""
        if stop_event is None:
            stop_event = threading.Event()
        print("Starting autoclicker...")
        try:
            while not stop_event.is_set():
                self.click_sequence(clicks_per_cycle, x, y, cycle_interval)
                if stop_event.is_set():
                    break
                time.sleep(self.get_delay() * 2)
        except KeyboardInterrupt:
            print("Autoclicker interrupted by user.")
        finally:
            print("Autoclicker session ended.")

if __name__ == "__main__":
    utils = ClickUtils()
    utils.click_sequence(3, 100, 100, 0.5)
    print("Demo completed.")