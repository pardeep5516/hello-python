from functools import wraps
import time


def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"executing ... {function.__name__}")
        ti = time.time()
        return_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-ti
        print(f"this function took {total_time} time")
    return wrapper

@calculate_time
def square_func(n):
    return [i**2 for i in range(1, n+1)]

square_func(1000)