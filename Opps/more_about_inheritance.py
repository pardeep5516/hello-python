
# ? multilevel inheritance
# ? method resolution order
# ? method overloading
# ? isinstance(), issubclass()


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, phone_number):
        print(f"calling{phone_number}.......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # Phone.__init__(self, brand, model_name, price)
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and {self._price}"


class FlashshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and {self._price} and {self.front_camera}"


onePlus = FlashshipPhone('onePlus', '6', 3800, '6gb', '64gb', "20MP", '16MP')
print(onePlus.full_name())


print(isinstance(onePlus,Phone))

print(issubclass(FlashshipPhone,Phone)) 


# print(help(FlashshipPhone))
