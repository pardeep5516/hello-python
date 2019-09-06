from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f" you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper



@print_function_data
def addition(a, b):
    """ this function take two number as argument and return there sum """
    return a + b


print(addition(4, 6))
