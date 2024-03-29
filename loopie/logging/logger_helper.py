'''
Created on Saturday 25/05/2019

@author: yaztown
'''

from loopie.logging import format_strings

import logging
import os
app_dirname, _ = os.path.split(os.path.dirname(os.path.abspath(__file__)))
default_log_dirname = os.path.join(app_dirname, 'log')


default_file_name='loopie.log'


def get_console_handler(level=logging.DEBUG):
    # Create handler
    hdl_console = logging.StreamHandler()
    hdl_console.setLevel(level)
    # Create formatters
    formatter_info = logging.Formatter(format_strings.fmt_simple_debug, datefmt=format_strings.fmt_date_small)
    hdl_console.setFormatter(formatter_info)
    return hdl_console

def get_file_handler(level=logging.DEBUG, log_dir=None, log_file=None):
    if log_file is None:
        log_file = default_file_name
    if log_dir is None:
        log_dir = default_log_dirname
    hdl_file = logging.FileHandler(os.path.join(log_dir, log_file), mode='w')
    hdl_file.setLevel(level)
    # Create formatters
    formatter_debug = logging.Formatter(format_strings.fmt_simple_debug, datefmt=format_strings.fmt_date_small)
    hdl_file.setFormatter(formatter_debug)
    return hdl_file

def get_logger(name='loopie', level=logging.DEBUG, log_dir=None, log_file=None):
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # Add handlers to the logger
    if not logger.hasHandlers():
        logger.addHandler(get_console_handler(level))
#         logger.addHandler(get_file_handler(level, log_dir, log_file))
    return logger


# example
# if __name__ == '__main__':
#     logger = get_logger('logger_helper')
#     
#     logger.debug('This is a debug')
#     logger.info('This is an info')
#     logger.warning('This is a warning')
#     logger.error('This is an error')
#     logger.critical('This is critical')
