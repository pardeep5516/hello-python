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


phone = Phone("nokia", '100', 1200)
smart_phone = Smartphone("onePlus", "6", 37000, "6gb", "64gb", "20mg")
print(smart_phone._price)
print(smart_phone.full_name())
