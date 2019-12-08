class Student:
    count = 0         # class variable
    def __init__(self):
        Student.count = Student.count + 1

s1=Student()
s2=Student()
s3=Student()

print("The number of students:",Student.count)

# Program for matrix

row = int(input("Enter Number of Rows: "))
columns = int(input("Enter number of columns : "))
matrix = []
print(type(matrix))
for i in range(row):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix.append(a)

print(matrix)