from typing import Dict, Any

class Config:
    """Configuration class for the autoclicker settings."""

    def __init__(self, settings: Dict[str, Any]) -> None:
        """Initializes the Config with the provided settings.

        Args:
            settings (Dict[str, Any]): A dictionary containing configuration settings.
        """
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key.

        Args:
            key (str): The key of the setting to retrieve.
            default (Any): The default value to return if the key doesn't exist.

        Returns:
            Any: The value associated with the given key, or default if not found.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Sets a configuration value by key.

        Args:
            key (str): The key of the setting to set.
            value (Any): The value to set for the specified key.
        """
        self.settings[key] = value

    def load_from_file(self, filepath: str) -> None:
        """Loads configurations from a specified file.

        Args:
            filepath (str): The path to the configuration file.
        """
        import json
        with open(filepath, 'r') as file:
            self.settings = json.load(file)  

    def save_to_file(self, filepath: str) -> None:
        """Saves current configurations to a specified file.

        Args:
            filepath (str): The path to the file where settings should be saved.
        """
        import json
        with open(filepath, 'w') as file:
            json.dump(self.settings, file, indent=4)
