# Class Inside Class (Inner Class)

class Student:                                    #Outer class
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        #self.lap = self.Laptop()               #Create object of laptop inside the Outer class

    def show(self):
        print(self.name , self.roll_no)
        #self.lap.show()

    class Laptop:                                   #Inner Class

        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram )  #, self.cpu, self.ram

s1 = Student('Akshay', 2)
s2 = Student('Rajat', 10)
print()

lap1 = Student.Laptop("dell","i5","8GB")
print()
lap1.show()

s1.show()
s2.show()





