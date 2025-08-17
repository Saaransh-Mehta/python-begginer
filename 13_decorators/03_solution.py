import time
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_run_function(a,b):
    time.sleep(4)
    print(a+b)
    return a + b
long_run_function(2,3)
long_run_function(2,3)