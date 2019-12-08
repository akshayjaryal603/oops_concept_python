# Types of methods
class Student:

    college = "IIT_Delhi"       # class/static variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

# Instance Method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

# Two types of Instance Method (Accessor & Mutator methods)

    def get_m1(self):               # Getters / Accessor
        return self.m1

    def set_m1(self, value):        # Setters / Mutator
        self.m1 = value
        print(Student.college)
        return self.m1


# Class Method
# Decorators
    @classmethod
    def info(cls):
        print()
        return cls.college

# Static methods

    @staticmethod
    def info1():
        print("\nThis is static method")

s1 = Student(45,47,98)
s2 = Student(85,75,89)

print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(s2.get_m1())

value = 1000
value1 = 800
print(s1.set_m1(value))
print(s2.set_m1(value1))
print(s1.avg())
print(Student.info())
Student.info1()
