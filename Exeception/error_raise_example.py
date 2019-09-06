# raise error example
# NotImplementedError
# abstract method


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Define sound method in subclass")


class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread

    def sound(self):
        return "dog sound"


class Cat(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread


doggy = Dog("tom", "jerry")
print(doggy.sound())
