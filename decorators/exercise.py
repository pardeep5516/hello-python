import time

t1 = time.time()
print("this is line one")
x = 5
if x == 5:
    print(f"x is equal to {x}")
print("this is line two")

for i in range(10):
    print(i)
t2 = time.time()
print(t2-t1)
