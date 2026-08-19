import logging

class Logger:
    """
    A simple logger class for the autoclicker.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the logger with a name and sets the log level.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """
        Logs a debug message.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Logs an informational message.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Logs a warning message.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Logs an error message.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Logs a critical message.
        """
        self.logger.critical(message)