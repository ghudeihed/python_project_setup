import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

class LoggingWrapper:
    """
    A wrapper for the Python logging module that sets up logging to both a file and the console.

    Attributes:
        logger (logging.Logger): The logger instance.
    """

    def __init__(self, name, log_dir='logs', log_level=logging.DEBUG, console_level=logging.ERROR, max_bytes=5*1024*1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = os.path.join(log_dir, f'log_{now}.log')
        fh = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)
    
    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)
    
    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
    
    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)
