import time
import threading
from collections import deque

class ActionQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, action):
        with self.lock:
            self.queue.append(action)

    def dequeue(self):
        with self.lock:
            if self.queue:
                return self.queue.popleft()
            return None

def autoclicker(delay, action_queue):
    while True:
        action = action_queue.dequeue()
        if action:
            action()  # Execute the action
        time.sleep(delay)

def start_autoclicker(delay):
    action_queue = ActionQueue()
    click_thread = threading.Thread(target=autoclicker, args=(delay, action_queue))
    click_thread.daemon = True
    click_thread.start()
    return action_queue

# Example of button click action

def click_action():
    print('Button clicked!')

if __name__ == '__main__':
    action_queue = start_autoclicker(0.1)
    for _ in range(10):
        action_queue.enqueue(click_action)
        time.sleep(0.2)