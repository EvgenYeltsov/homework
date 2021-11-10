# Task 2_15_1
"""
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"
"""
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return print(f"{func.__name__} called with {args}")
    return wrapper


@logger
def add_(x, y):
    return x + y


@logger
def square_all(*args):
    return


add_(4, 6)
square_all(1, 2, 36, 67)
