class Laptop:
    def __init__(self, brand, model_name, price):
        # instance variable
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self, num):
        # self.price
        off_price = (num/100)*self.price
        return self.price - off_price


laptop1 = Laptop("asus", "xu507", 37000)
laptop2 = Laptop("asus", "xu507", 37000)
print(laptop1.apply_discount(10))
print(laptop2.apply_discount(50))
