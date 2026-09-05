import logging
import sys
from pathlib import Path
from typing import Optional

DEFAULT_LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ClickerLogger:
    """Centralized logging manager for the autoclicker application."""

    def __init__(self, log_file: Optional[Path] = None, debug: bool = False):
        self.logger = logging.getLogger("AutoClicker")
        self.logger.setLevel(logging.DEBUG if debug else logging.INFO)
        self.logger.handlers.clear()

        # Standard console handler setup
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT, datefmt=DATE_FORMAT))
        self.logger.addHandler(console_handler)

        # Optional persistent file logging
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT, datefmt=DATE_FORMAT))
            self.logger.addHandler(file_handler)

    def log_action(self, action: str, x: int, y: int) -> None:
        """Log mouse actions with screen coordinates."""
        self.logger.debug("Action '%s' triggered at coordinates (%d, %d)", action, x, y)

    def log_status(self, active: bool, interval: float) -> None:
        """Log state changes and current click interval configuration."""
        state = "STARTED" if active else "STOPPED"
        self.logger.info("Engine %s | Target interval: %.3fs", state, interval)

    def get_logger(self) -> logging.Logger:
        """Return raw logger instance."""
        return self.logger


def setup_logger(log_file: Optional[str] = None, debug: bool = False) -> logging.Logger:
    """Helper function to initialize logging setup."""
    path = Path(log_file) if log_file else None
    manager = ClickerLogger(log_file=path, debug=debug)
    return manager.get_logger()
