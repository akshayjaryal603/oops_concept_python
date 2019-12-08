# How Constructor behaves in Inheritance
# How to use Super() in Inheritance
# Method resolution Order(MRO)

class A:
    count = 1
    def __init__(self):
        a = 1
        print("Init method of A")

    def feature1(self):
        print("Inside feature 1")

    def feature2(self):
        print("Inside feature 2")

class B:
    def __init__(self):
        #super().__init__()
        print("Init method of B")

    def feature5(self):
        super().feature1()
        print("Inside feature 5")

    def feature6(self):
        print("Inside feature 6")

# Use of Super Keyword
# MRO (Method Resolution Order)
class C(A,B):
    def __init__(self):
        #A().__init__()
        super().__init__()
        print("Init method of C")

    def feature3(self):
        print("Inside feature 3")

    def feature4(self):
        #super().feature2()
        print("Inside feature 4")

a1 = C()

#a1.feature5()

#a1.feature4()
