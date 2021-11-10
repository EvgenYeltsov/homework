# Task 2_15_2
"""Write a decorator that takes a list of stop words and replaces them with * inside the decorated function"""
from functools import wraps


def stop_world(word1):
    def inner_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for word in word1:
                if word in res:
                    res = res.replace(word, "*")
            return res
        return wrapper
    return inner_wrapper


@stop_world(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Steve'))
