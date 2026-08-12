from typing import Optional, Tuple

class AutoClicker:
    def __init__(self, click_interval: float, repetitions: Optional[int] = None) -> None:
        """
        Initializes the AutoClicker with a click interval and optional repetitions.

        Args:
            click_interval (float): The time interval between clicks in seconds.
            repetitions (Optional[int]): The number of clicks to perform. If None, clicks indefinitely.
        """
        self.click_interval = click_interval
        self.repetitions = repetitions
        self.running = False

    def start(self) -> None:
        """
        Starts the auto-clicking process.
        """
        if self.running:
            return
        self.running = True
        self._click_loop()

    def stop(self) -> None:
        """
        Stops the auto-clicking process.
        """
        self.running = False

    def _click_loop(self) -> None:
        """
        The loop that performs the clicking at the specified interval.
        """
        import time
        clicks_performed = 0

        while self.running:
            self._perform_click()
            clicks_performed += 1
            if self.repetitions is not None and clicks_performed >= self.repetitions:
                break
            time.sleep(self.click_interval)

    def _perform_click(self) -> None:
        """
        Simulates a click event.
        """
        print("Click!")  # Replace with actual click logic

if __name__ == '__main__':
    auto_clicker = AutoClicker(0.5, 10)  # Click every 0.5 seconds, up to 10 times
    auto_clicker.start()  # Start clicking
