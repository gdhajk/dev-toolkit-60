import time
import random

class AutoClicker:
    def __init__(self, interval=0.1, clicks=1):
        self.interval = interval  # time between clicks
        self.clicks = clicks      # number of clicks

    def perform_clicks(self):
        for _ in range(self.clicks):
            self.click()
            time.sleep(self.interval)

    def click(self):
        # Simulating a click action
        print('Click!')  # Placeholder for actual click functionality

    def set_interval(self, interval):
        self.interval = interval

    def set_clicks(self, clicks):
        self.clicks = clicks

def random_interval(min_interval=0.05, max_interval=0.5):
    return random.uniform(min_interval, max_interval)

if __name__ == '__main__':
    auto_clicker = AutoClicker()  # default interval and clicks
    auto_clicker.perform_clicks()  # Execute clicks
