class Student:
    # Constructor - parameterized
    def __init__(self, name, roll_no):
        print("This is parametrized constructor")
        self.name = name
        self.roll_no = roll_no

    def show(self):
        print("Name: %s" %self.name)
        print("Roll no %d" %self.roll_no)

student = Student("John" , 30)
student.show()