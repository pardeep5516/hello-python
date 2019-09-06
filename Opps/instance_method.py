class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return (f"First Name {self.first_name} Last Name {self.last_name}")

    def is_above_18(self):
        return self.age >10


p1 = Person('alex', 'aha', 10)
p2 = Person("alice", 'tom', 22)
# print(p2.full_name()) # same as print(Person.full_name(p2))
print(p1.is_above_18())

l = [1, 2, 3, 4, 5]
#clear , pop
# l.clear()
# list.clear(l)
l.append(10) #list.append(l,10)
# print(l)
