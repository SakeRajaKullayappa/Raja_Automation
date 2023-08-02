class Computer:

    def __init__(self):
        self.name = "Raja"
        self.age = 26

    def compair(self, others):
        if self.age == others.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.age = 40

if c1.compair(c2):
    print("They are same age")
else:
    print("They are not same age")

print(c1.name)
print(c2.name)
