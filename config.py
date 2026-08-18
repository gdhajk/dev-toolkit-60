import os

class Config:
    def __init__(self):
        self.load_config()

    def load_config(self):
        self.settings = {
            'click_delay': self.get_env_variable('CLICK_DELAY', 0.1),
            'max_clicks': self.get_env_variable('MAX_CLICKS', 1000),
            'click_button': self.get_env_variable('CLICK_BUTTON', 'left')
        }

    def get_env_variable(self, var_name, default):
        return float(os.getenv(var_name, default))

    def get_setting(self, key):
        return self.settings.get(key)

config = Config()  # Create a global config instance
