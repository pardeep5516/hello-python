import time
#list va generator
#when used list , when used generator
t1 = time.time()
l = [i**2 for i in range(10000000)] #10milion
t2 = time.time() - t1
print(t2)
#g = (i**2 for i in range(10000000)) #10milion