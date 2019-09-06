class Person:
    count_instance = 0  # class variable

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(",")
        return cls(first,last, age)

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instance of {cls.__name__} class"

    def full_name(self):
        return (f"First Name {self.first_name} Last Name {self.last_name}")

    def is_above_18(self):
        return self.age > 18


p1 = Person('alex', 'aha', 10)
p2 = Person("alice", 'tom', 22)

p3 = Person.from_string("tom,jerry,23")
print(p3.full_name())

# print(Person.count_instances())
