import time
import threading

class AutoClicker:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = False
        self.click_thread = None

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self._click_loop)
            self.click_thread.start()

    def stop_clicking(self):
        if self.running:
            self.running = False
            self.click_thread.join()

    def _click_loop(self):
        while self.running:
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        print("Click!")  # Replace with actual click logic

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    clicker.start_clicking()
    time.sleep(5)
    clicker.stop_clicking()