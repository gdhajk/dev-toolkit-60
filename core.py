import time

class AutoClicker:
    def __init__(self, interval):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        print('AutoClicker started')
        while self.running:
            self.click()
            time.sleep(self.interval)

    def click(self):
        print('Click!')  # Simulate a mouse click

    def stop(self):
        self.running = False
        print('AutoClicker stopped')

    def set_interval(self, new_interval):
        self.interval = new_interval
        print(f'Interval set to {self.interval} seconds')