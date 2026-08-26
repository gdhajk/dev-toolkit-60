import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "dev-toolkit-60", log_file: str = "autoclicker.log", max_bytes: int = 5 * 1024 * 1024, backup_count: int = 3) -> logging.Logger:
    """Configure and return a logger with rotating file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers if setup is called multiple times
    if logger.hasHandlers():
        return logger
        
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Console handler for standard output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Rotating file handler to prevent excessive disk usage
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    logger.info("Logger setup completed successfully")
    return logger

logger = setup_logger()
