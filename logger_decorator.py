# Decorator wraps a function and changes its behavior.
import logging
import time
from functools import wraps
from datetime import datetime


def my_logger(orig_func):
    """Decorator that logs the name of function,
       its arguments and results of the function."""
    logging.basicConfig(filename=f'{orig_func.__name__}.log',
                        level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        """Here might be some computations"""
        result = orig_func(*args, **kwargs)
        logging.info(f'The func {orig_func.__name__} run with\n'
                     f'- args: {args}\n'
                     f'- kwargs: {kwargs}\n\n'
                     f'Result: {result}')
        return orig_func(*args, **kwargs)
    
    return wrapper


def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'The orig_func: {orig_func.__name__} ran in {t2} seconds'
              f'result is: {result}')
        return result
    return wrapper
