import logging
import sys
from typing import Optional


class AutoclickerLogger:
    """Provides a standardized logging interface for the dev-toolkit-60 autoclicker."""

    def __init__(self, name: str = "autoclicker", level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log a general information message."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message: str, exc_info: Optional[bool] = None) -> None:
        """Log an error message with optional exception info."""
        self.logger.error(message, exc_info=exc_info)


def get_logger(name: str) -> AutoclickerLogger:
    """Factory function to instantiate a configured logger."""
    return AutoclickerLogger(name=name)
