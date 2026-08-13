import logging
from logging.handlers import RotatingFileHandler

# Configure logger settings
def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    logger = logging.getLogger(__name__)
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

# Example usage of setup_logger
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up successfully!')