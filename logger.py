import logging

# Configure the logger for the autoclicker
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class AutoClickerLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Example usage of the logger
if __name__ == '__main__':
    clicker_logger = AutoClickerLogger('AutoClicker')
    clicker_logger.info('AutoClicker started successfully.')
    clicker_logger.warning('This is a warning message.')
    clicker_logger.error('This is an error message.')