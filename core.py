import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval  # time in seconds
        self.running = False
        self.click_thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.start()

    def stop(self):
        self.running = False
        if self.click_thread:
            self.click_thread.join()  # wait for thread to finish

    def _click_loop(self):
        while self.running:
            self.single_click()
            time.sleep(self.interval)

    def single_click(self):
        # Add actual clicking mechanism here
        print('Click!')

# Example usage:
if __name__ == '__main__':
    auto_clicker = AutoClicker(interval=0.05)
    auto_clicker.start()
    time.sleep(1)  # Let it click for a second
    auto_clicker.stop()
