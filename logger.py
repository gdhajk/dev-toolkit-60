import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """
    Set up a rotating logger.

    Parameters:
    log_file (str): The name of the log file.
    max_bytes (int): Maximum size of the log file before rotation.
    backup_count (int): Number of backup log files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready to go!')