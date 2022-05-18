from functools import wraps

def validate(low_bound: int, upper_bound: int) -> callable:
    """Returns function decorator that applies arguments validation."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def inner(*args, **kwargs) -> str:
            """Checks whether all arguments are in bounds."""
            for arg in args:
                if (arg not in range(low_bound, upper_bound+1)):
                    return 'Function call is not valid!'
    
            return func(*args, **kwargs)
    
        return inner
    
    return decorator


@validate(low_bound=0, upper_bound=256)
def set_pixels(red, green, blue):
    print('Pixel created!')