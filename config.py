import json
import os

DEFAULTS = {
    'click_interval': 0.1,
    'click_count': 100,
    'mouse_button': 'left',
    'enable_logging': True
}

class ConfigLoader:
    def __init__(self, filepath='config.json'):
        self.filepath = filepath
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                try:
                    user_config = json.load(file)
                except json.JSONDecodeError:
                    print('Error decoding JSON, using defaults.')
                    return DEFAULTS
            return {**DEFAULTS, **user_config}
        else:
            print('Config file not found, using defaults.')
            return DEFAULTS

    def get(self, key):
        return self.config.get(key, DEFAULTS.get(key))

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)  # Print loaded configuration for testing
