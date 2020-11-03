import logging
from functools import wraps
from datetime import datetime


def my_logger(orig_func):
    logging.basicConfig(filename=f'{orig_func.__name__}.log',
                        level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        result = orig_func(*args, **kwargs)
        logging.info(f'The func {orig_func.__name__} run with\n'
                     f'- args: {args}\n'
                     f'- kwargs: {kwargs}\n\n'
                     f'Result: {result}')
        return orig_func(*args, **kwargs)
    
    return wrapper
