# to create first generator with generator function
# 1 : )generator function
# 2 :) generator comprehension


def num(n):
    for i in range(1, n+1):
        yield i # or yield(i)



numbers = num(10)
for num in numbers:
    print(num)

# for number in num(10):
#     print(number)

# print(num(10))
