# map function

number = [1, 2, 3, 4]


# def square(a):
#     return a**2


# squares = list(map(square, number))

#with lambda function 
squares = list(map(lambda a:a**2, number))
# print(squares)

#with list comprehension
squares = [i**2 for i in number]
# print(squares)

#without any function 

new_list  = []
for num in number:
    new_list.append(num**2)

print(new_list)

names = ['abc','abcd','abcde']
length = list(map(len,names))

print(length)
# for i in length:
#     print(i)


# for j in length:
#     print(j)