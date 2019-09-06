#magic method / dunder method
#operator overloading
#polymorphism


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price


    def phone_name(self):
        return f"{self.brand} {self.model_name}"

    #str , repr

    def __str__(self):
          return f"{self.brand} {self.model_name} {self.price}"


    def __repr__(self):
        return f"Phone('{self.brand}' '{self.model_name}' {self.price})"

    def __len__(self):
        return len(self.phone_name())

    def __add__(self, other):
        return self.price + other.price



class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # Phone.__init__(self, brand, model_name, price)
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def phone_name(self):
        return f"{self.brand} {self.model_name} and {self.price} "

    def __len__(self):
        return len(self.phone_name())

phone1 = Phone("nokia", 1100, 1200)
phone2 = Phone("nokia", 1100, 1200)
onePlus = Smartphone('onePlus', '6', 3800, '6gb', '64gb', "20MP")

print(onePlus.phone_name())
print(len(onePlus))
print(len(phone1))
# print(phone1.phone_name())

#print(phone1 + phone2)



# print(str(phone1))
# print(repr(phone1))

#print(len(phone1))
