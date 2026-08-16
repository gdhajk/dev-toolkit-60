import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=1024 * 1024 * 5, backup_count=5):
    """Sets up a rotating logger."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    
    return logger

# Example of setting up the logger
if __name__ == '__main__':
    my_logger = setup_logger()
    my_logger.info('Logger is set up and ready to go!')