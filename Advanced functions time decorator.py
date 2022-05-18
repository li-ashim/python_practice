from time import time

def time_decorator(func):
    def inner(*args, **kwargs):
        time_start = time()
        func(*args, **kwargs)
        time_end = time()
        print(f'Execution of {func.__name__} function took {time_end - time_start}')
    
    return inner

@time_decorator
def foo():
    print('Foo')
    l = []
    for i in range(1_000_000_0):
        l.append(i)
        l.pop()
