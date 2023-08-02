class FatherClass:

    def feature1(self):
        print("Working 1 Feature")

    def feature2(self):
        print("Working 2 Feature")


class SonClass(FatherClass):

    def feature3(self):
        print("Working 3 Feature")

    def feature4(self):
        print("Working 4 Feature")


class GrandSonClass(SonClass):

    def feature5(self):
        print("Working 5 Feature")


fat1 = FatherClass()
fat1.feature1()
fat1.feature2()

son1 = SonClass()
son1.feature1()
son1.feature2()
son1.feature3()
son1.feature4()

gSon = GrandSonClass()
gSon.feature1()
gSon.feature2()
gSon.feature3()
gSon.feature4()
gSon.feature5()

print("====================================================")


class GrandFather:

    def __init__(self):
        print("Init for GrandFather Class ")

    def feature1(self):
        print("Working 1 Feature")

    def feature2(self):
        print("Working 2 Feature")


class Father(GrandFather):

    def __init__(self):
        super().__init__()
        print("Init for Father Class ")

    def feature3(self):
        print("Working 3 Feature")

    def feature4(self):
        print("Working 4 Feature")


class Son(Father):

    def __init__(self):
        super().__init__()
        print("Init for Son Class ")

    def feature5(self):
        print("Working 5 Feature")


son = Son()