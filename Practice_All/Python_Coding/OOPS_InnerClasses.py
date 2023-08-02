class Student:

    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "Lenovo"
            self.CPU = "i5"
            self.ram = "16gb"

        def show(self):
            print(self.brand, self.CPU, self.ram)


s1 = Student("Raja", 395)
s2 = Student("Teja", 595)

s1.show()
s2.show()
