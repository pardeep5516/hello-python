


f =open('file1.txt')
# print(f"cursor position {f.tell()}")
# print(f.read())
# print(f.readline(),end = "")
# print(f.readline())
# print(f"cursor position {f.tell()}")
# print("before seek method")
# print(f"cursor position {f.tell()}")
# f.seek(0)
# print("after seek method")
# print(f"cursor position {f.tell()}")

# print(f.readlines())

# for line in f.readlines():
#     print(line)
#name, closed
print(f.name)
f.close()
print(f.closed)