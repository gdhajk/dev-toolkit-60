import time
import threading
import pyautogui

pyautogui.FAILSAFE = True

class ClickerHelper:
    """Provides helper methods for autoclicker functionality."""

    def __init__(self):
        self.is_running = False
        self.click_interval = 0.5
        self.target_position = (100, 100)
        self.click_thread = None

    def update_settings(self, interval=None, position=None):
        if interval is not None:
            self.click_interval = max(0.01, interval)
        if position is not None:
            self.target_position = position

    def _perform_click(self):
        try:
            pyautogui.moveTo(self.target_position[0], self.target_position[1])
            pyautogui.click()
        except Exception:
            pass

    def _click_loop(self):
        while self.is_running:
            self._perform_click()
            time.sleep(self.click_interval)

    def start_clicking(self):
        if self.is_running:
            return False
        self.is_running = True
        self.click_thread = threading.Thread(target=self._click_loop)
        self.click_thread.daemon = True
        self.click_thread.start()
        return True

    def stop_clicking(self):
        self.is_running = False
        if self.click_thread and self.click_thread.is_alive():
            self.click_thread.join(timeout=2.0)
        return True

    def get_status(self):
        return {
            "running": self.is_running,
            "interval": self.click_interval,
            "position": self.target_position
        }

    def set_position_from_mouse(self):
        pos = pyautogui.position()
        self.target_position = (pos.x, pos.y)
        return self.target_position