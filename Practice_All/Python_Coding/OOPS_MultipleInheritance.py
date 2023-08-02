# class FatherClass:
#
#     def feature1(self):
#         print("Working 1 Feature")
#
#     def feature2(self):
#         print("Working 2 Feature")
#
#
# class MotherClass:
#
#     def feature3(self):
#         print("Working 3 Feature")
#
#     def feature4(self):
#         print("Working 4 Feature")
#
#
# class SonClass(FatherClass, MotherClass):
#
#     def feature5(self):
#         print("Working 5 Feature")
#
#
# fat1 = FatherClass()
# fat1.feature1()
# fat1.feature2()
#
# mot1 = MotherClass
# mot1.feature3()
# mot1.feature4()
#
#
# son1 = SonClass
# son1.feature1()
# son1.feature2()
# son1.feature3()
# son1.feature4()
# son1.feature5()


print("==============================================================")


class FatherClass:

    def __init__(self):
        print("Init for FatherClass")

    def feature1(self):
        print("Working 1 Feature")

    def feature2(self):
        print("Working 2 Feature")


class MotherClass:

    def __init__(self):
        print("Init for MotherClass")

    def feature3(self):
        print("Working 3 Feature")

    def feature4(self):
        print("Working 4 Feature")


class SonClass(FatherClass, MotherClass):
    
    def __init__(self):
        super().__init__()
        print("Init for SonClass")

    def feature5(self):
        print("Working 5 Feature")

son = SonClass()