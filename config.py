import json
from typing import Any, Dict

class ConfigurationError(Exception):
    pass

class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any]):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_from_file(self, filepath: str) -> None:
        try:
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)
        except FileNotFoundError:
            raise ConfigurationError(f'Configuration file not found: {filepath}')
        except json.JSONDecodeError:
            raise ConfigurationError(f'Error decoding JSON from: {filepath}')

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

# Example default configuration
DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False
}

# Usage
# loader = ConfigLoader(DEFAULT_CONFIG)
# loader.load_from_file('config.json')
# db_host = loader.get('host')