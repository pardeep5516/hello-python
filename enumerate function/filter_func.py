# filter function


def is_even(a):
    return a % 2 == 0


numbers = [3, 4, 5, 6, 3, 6, 3, 79]

# evens = tuple(filter(is_even,numbers))

evens = tuple(filter(lambda a:a%2==0,numbers))

# evens = filter(lambda a:a%2==0,numbers)
for i in evens:

    print(i,end="")

for i in evens:

    print(i,end="")


#with list comp
evens2 = [i for i in numbers if i%2==0]
print(evens2)