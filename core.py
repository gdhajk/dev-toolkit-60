import time
from threading import Thread
from pynput.mouse import Button, Controller

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval  
        self.running = False
        self.mouse = Controller()

    def start_clicking(self):
        self.running = True
        while self.running:
            self.mouse.click(Button.left)
            time.sleep(self.interval)

    def stop_clicking(self):
        self.running = False

    def toggle(self):
        if not self.running:
            Thread(target=self.start_clicking).start()
        else:
            self.stop_clicking()

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.1)
    try:
        clicker.toggle()  # Starts clicking
        time.sleep(5)  # Click for 5 seconds
    finally:
        clicker.stop_clicking()  # Ensure clicking stops
