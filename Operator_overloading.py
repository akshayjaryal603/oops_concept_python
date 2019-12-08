#Example 1 of Operator Overloading in Polymorphism

a,b=10,20
c,d=-10.5,0
print(int.__add__(a,b))
print(float.__abs__(c))
print(int.__bool__(d))
print(str.__add__(str(a),str(b)))
print(int.__gt__(a,b))

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = Student(m1,m2)
        return s3

s1 = Student(60,90)
s2 = Student(30,80)

s3 = s1+s2              #Student.__add__(s1,s2)
print()
print(s3.m1)
print()
print(s3.m2)

