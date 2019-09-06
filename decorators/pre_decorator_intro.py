

def square(n):
    return n**2

# print(square(7))

s = square

print(s(7))
print(s.__name__)
print(square.__name__)

print(s)
print(square)