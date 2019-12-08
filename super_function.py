class A:
    count = 1
    def __init__(self):
        a = 1
        print("Init method of A")

    def feature1(self):
        print("Inside feature 1")

    def feature2(self):
        print("Inside feature 2")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init method of B")

    def feature5(self):
        super().feature1()
        print("Inside feature 5")

    def feature6(self):
        print("Inside feature 6")

class C(B):
    def __init__(self):
        super().__init__()
        print("Init method of C")

    def feature3(self):
        super().feature1()
        print("Inside feature 3")

    def feature4(self):
        print("Inside feature 5")

obj = C()
obj.feature5()
obj.feature1()
obj.feature2()
obj.feature6()