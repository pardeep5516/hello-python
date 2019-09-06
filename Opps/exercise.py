class Laptop:
    def __init__(self, brand, model_name, price):
        # instance variable
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name


laptop1 = Laptop("asus", "xu507", 37000)
print(laptop1.laptop_name)
