# lambda expression practiced

# def is_even(a):
#     if a %2==0:
#         return True
#     else:
#         return False


# def is_even(a):
#     return a % 2 == 0  # return true or false


# print(is_even(3))

# is_even2 = lambda a:a%2==0
# print((is_even2(6)))

# def last_char(s):
#     return s[-1]


# last_char2 = lambda s:s[-1]
# print(last_char2("alex"))

# lambda with is else
def func(s):
    return len(s) > 5
        

# func2 = lambda s:True if len(s)>5 else False
# print(func2('abs'))

func2 = lambda s: len(s)>5 
print(func2('abs'))