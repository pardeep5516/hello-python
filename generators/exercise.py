def gen_func(n):
    for i in range(1,n+1):
        if i %2 == 0:
            yield i

number = gen_func(5)
for i in number:
    print(i)