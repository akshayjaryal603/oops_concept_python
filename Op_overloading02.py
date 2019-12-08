#Example 2 of Operator Overloading in Polymorphism

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>s2:
            return True
        else:
            return False

s1 = Student(60,90)
s2 = Student(30,80)

#Compare two objects

if s1>s2:
    print("\ns1 wins")
else:
    print("\ns2 wins")