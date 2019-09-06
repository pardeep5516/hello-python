# any all


def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        print("wrong input")


print(my_sum(*[2, 4, 5, 4.5]))
