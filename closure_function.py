"""
Написать функцию, которая обертывает любую передаваемую в нее
функцию и возвращает кортеж[имя функции, значение]
"""

def deanon(func: callable) -> callable:
    def inner(*args, **kwargs):
        return (func.__name__, func(*args, **kwargs))
    
    return inner