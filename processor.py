import time

class InputValidationError(Exception):
    pass

def validate_click_interval(interval):
    if not isinstance(interval, (int, float)):
        raise InputValidationError('Interval must be a number.')
    if interval <= 0:
        raise InputValidationError('Interval must be greater than zero.')

class AutoClicker:
    def __init__(self, click_interval):
        validate_click_interval(click_interval)
        self.click_interval = click_interval

    def start_clicking(self):
        try:
            print('AutoClicker started with an interval of', self.click_interval)
            while True:
                self.perform_click()
                time.sleep(self.click_interval)
        except KeyboardInterrupt:
            print('AutoClicker stopped by user.')

    def perform_click(self):
        # Simulate the click event
        print('Click!')

if __name__ == '__main__':
    click_interval = 0.5  # Set your click interval here
    auto_clicker = AutoClicker(click_interval)
    auto_clicker.start_clicking()