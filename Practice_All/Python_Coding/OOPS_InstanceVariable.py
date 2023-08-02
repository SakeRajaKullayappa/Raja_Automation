class Car:

    engine = "BS6"

    def __init__(self):
        self.milage = 10
        self.company = "BMW"

    def compair(self, others):
        if self.engine == others.engine:
            return True
        else:
            return False


c1 = Car()
c2 = Car()

Car.engine = "BS7"

if c1.compair(c2):
    print("c1 and c2 objs milage and company names are same ")
else:
    print("c1 and c2 objs milage and company names are not same ")


print(c1.milage, c1.company, c1.engine)
print(c2.milage, c2.company, c2.engine)
