import time
import threading

class AutoClicker:
    def __init__(self, delay):
        self.delay = delay
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _click(self):
        while self.running:
            self._perform_click()
            time.sleep(self.delay)

    def _perform_click(self):
        print('Click!')  # Simulating a click action

if __name__ == '__main__':
    clicker = AutoClicker(0.1)  # 10 clicks per second
    clicker.start()
    time.sleep(1)  # Let it click for 1 second
    clicker.stop()  # Stop clicking