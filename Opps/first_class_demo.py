class Persion:
    def __init__(self, first_name, last_name, age):
        #instance variable
        print("init  method / constructor get call")
        self.first_name = first_name #object.first_name
        self.last_name = last_name
        self.age = age


p1 = Persion("alex", "sha", 20)
p2 = Persion("alice", "tom", 21)

print(p1.first_name)
# print(p2.first_name)