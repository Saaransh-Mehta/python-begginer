def get_name(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling : {func.__name__} . total args = {args_value} kw_args = {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@get_name
def sum_all(*args):
    return sum(*args)

sum_all((1,2,3,4,5,6,7,8,9,0))