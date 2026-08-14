import time
import random

class AutoClicker:
    def __init__(self, click_interval):
        self.click_interval = click_interval

    def validate_click_interval(self):
        if not isinstance(self.click_interval, (int, float)):
            raise ValueError('Click interval must be a number.')
        if self.click_interval <= 0:
            raise ValueError('Click interval must be greater than zero.')

    def click(self):
        print('Click!')

    def run(self):
        self.validate_click_interval()
        print('Starting auto clicker...')
        try:
            while True:
                self.click()
                time.sleep(self.click_interval)
        except KeyboardInterrupt:
            print('Auto clicker stopped.')

if __name__ == '__main__':
    click_interval = random.uniform(0.1, 2.0)  # Simulate user input
    clicker = AutoClicker(click_interval)
    clicker.run()