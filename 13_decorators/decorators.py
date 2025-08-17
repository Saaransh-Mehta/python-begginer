import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time= time.time()
        print(f"Start time is {start_time} and end time of function is {end_time}")
        return result
    return wrapper

@timer
def sum_all(*args):
    result = sum(*args)
    return result

sum_all((1,2,3,4,5,6,7,8,9))
