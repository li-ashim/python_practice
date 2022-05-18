from typing import Callable


def deanon(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        return (func.__name__, func(*args, **kwargs))
    
    return inner

def foo(a, b):
    return a + b