import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.load_config()

    def load_config(self):
        if not os.path.isfile(self.filepath):
            raise ConfigError(f'Config file not found: {self.filepath}')
        try:
            with open(self.filepath, 'r') as f:
                self.config_data = json.load(f)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from config file')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        if key in self.config_data:
            return self.config_data[key]
        return default

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.config_data, f, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving config: {str(e)}')

# Example usage:
if __name__ == '__main__':
    config = Config('config.json')
    print(config.get('some_key', 'default_value'))
    config.set('new_key', 'new_value')