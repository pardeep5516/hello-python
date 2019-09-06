class Laptop:
    discount_persent = 10

    def __init__(self, brand, model_name, price):
        # instance variable
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self):
        # self.price
        off_price = (self.discount_persent/100)*self.price
        return self.price - off_price


laptop1 = Laptop("asus", "xu507", 37000)
laptop2 = Laptop("asus", "xu507", 37000)
laptop2.discount_persent = 50
print(laptop2.apply_discount())
print(laptop2.__dict__)


"""
class Circle:
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius
        

    def calc_circumference(self):
        return 2*Circle.PI*self.radius

c= Circle(5)
print(c.calc_circumference())   """
