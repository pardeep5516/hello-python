#iterator vs iterables

numbers = [1,2,3,4]#iterables

square = map(lambda a:a**2,numbers)#iterator

# for i in numbers:
#     print(i)


#call iter function 
#iter(numbers)------> iterator
#next(iter(numbers))

# number_iter = iter(numbers)
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))#Exception

print(next(square))
print(next(square))
print(next(square))