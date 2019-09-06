class A:
    def class_a_method(self):
        return 'I\'m just class a method'

    def hello(self):
        return "hello from class a"


class B:
    def class_b_method(self):
        return 'I\'m just class b method'

    def hello(self):
        return "hello from class b"


class C(A, B):
    pass


instance_c = C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())

# print(help(C))
print(C.mro())

