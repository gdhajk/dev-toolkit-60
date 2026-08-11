import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10240, backup_count=5):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler that logs debug and higher level messages
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    
    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage:
if __name__ == '__main__':
    log = setup_logger()
    log.debug('Debug message')
    log.info('Info message')
    log.warning('Warning message')
    log.error('Error message')
    log.critical('Critical message')