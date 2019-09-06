# any all function

number1 = [3, 4, 7, 7, 10]
number2 = [1, 3, 5, 7, 9]


print(all([num%2==0 for num in number1]))
print(any([num%2==0 for num in number1]))




evens1 = []
# for num in number1:
#     if num%2==0:
#         evens1.append(True)


for num in number1:
    evens1.append(num % 2 == 0)



# print(all([False, True, True, True, True]))
# print(evens1)

# print(all([num%2==0 for num in number1]))
