def add(a, b):
    if (type(a) is int) and (type(b)is int):
        return a+b
    raise TypeError("oops wrong data type")
print(add('4','5'))