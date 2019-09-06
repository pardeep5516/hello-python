# encapsulation
# Abstraction
# naming convention
# name mangling..........> __name


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"calling{phone_number}.......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass


phone1 = Phone("nokia", 1100, 1200)
# phone1._price = 100


# print(phone1.__price)

phone1._Phone__price = 1900

print(phone1._Phone__price)
print(phone1.__dict__)


# _name    # convention for private name
# __name__ # dunder/magic method
