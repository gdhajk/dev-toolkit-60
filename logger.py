import logging
import sys
from datetime import datetime

class ClickerLogger:
    def __init__(self, name: str = "dev-toolkit-60") -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)

logger = ClickerLogger()