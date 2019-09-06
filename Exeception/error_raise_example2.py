
class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobile = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobile.append(new_mobile)
        else:
            raise TypeError("new mobile should be object of  mobile class")

onePlus = Mobile("one plus 7")
samsung = "samsung galaxy s10"
mobo_store = MobileStore() 
# mobo_store.add_mobile(samsung)
mobo_store.add_mobile(onePlus)
mobo = mobo_store.mobile
print(mobo[0].name)