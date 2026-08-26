import time
import threading

class HighPerformanceAutoclicker:
    """Optimized core engine for high-frequency clicking operations."""
    
    def __init__(self, cps: float):
        self.interval = 1.0 / float(cps)
        self.running = False
        self._thread = None

    def _click_loop(self) -> None:
        """High-resolution timing loop minimizing CPU overhead."""
        target_time = time.perf_counter()
        while self.running:
            target_time += self.interval
            current_time = time.perf_counter()
            
            sleep_duration = target_time - current_time
            if sleep_duration > 0:
                time.sleep(sleep_duration)
            else:
                # Reset target if system is lagging to prevent burst catching
                target_time = current_time

    def start(self) -> None:
        """Start the autoclicker thread."""
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        """Stop the autoclicker thread cleanly."""
        self.running = False
        if self._thread:
            self._thread.join(timeout=1.0)
            self._thread = None

    def update_cps(self, cps: float) -> None:
        """Dynamically update clicks per second rate."""
        self.interval = 1.0 / float(cps)
