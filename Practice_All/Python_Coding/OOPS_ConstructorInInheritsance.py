class Father:

    def __init__(self):
        print("Init in Father Class")

    def feature1(self):
        print("Working 1 Feature")

    def feature2(self):
        print("Working 2 Feature")


class Daughter(Father):

    def __init__(self):
        super().__init__()
        print("Init in Daughter Class")

    def feature3(self):
        print("Working 3 Feature")

    def feature4(self):
        print("Working 4 Feature")


daughter = Daughter()


