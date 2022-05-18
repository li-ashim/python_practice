from functools import reduce

class Cache:
    def __init__(self, use_cache=True) -> None:
        self.use_cache = use_cache
        self.cache = dict()
        
    def __call__(self, func):
        def inner(*args, **kwargs):
            key = reduce(lambda r1, r2: r1 + '_' + r2, 
                         map(repr, args), '')
            key += reduce(lambda r1, r2: r1 + '_' + r2, 
                          map(repr, kwargs.items()), '')
            print(key)
            if self.use_cache and (key in self.cache):
                return self.cache[key]
            else:
                res = func(*args, **kwargs)
                self.cache[key] = res
                return res
        return inner
