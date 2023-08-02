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


fat1 = FatherClass()
fat1.feature1()
fat1.feature2()

son1 = SonClass()
son1.feature1()
son1.feature2()
son1.feature3()
son1.feature4()


print("======================================================================")

#
# class Father:
#
#     def __init__(self):
#         print("Init in Father Class")
#
#     def feature1(self):
#         print("Working 1 Feature")
#
#     def feature2(self):
#         print("Working 2 Feature")
#
#
# class Daughter(Father):
#
#     def __init__(self):
#         super().__init__()
#         print("Init in Daughter Class")
#
#     def feature3(self):
#         print("Working 3 Feature")
#
#     def feature4(self):
#         print("Working 4 Feature")
#
#
# daughter = Daughter()


