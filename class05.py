class CSStudent:
    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll,stream):
        # Instance Variable
        self.roll = roll
        self.stream = stream

    # Objects of CSStudent class

a = CSStudent(101,"Ece")
b = CSStudent(102,"Mech")

print(a.stream)     # prints "cse"
print(b.stream)     # prints "cse"
print(a.roll)       # prints 101
print(b.roll)

# Class variables can be accessed using class name also

print(CSStudent.stream)  # prints "cse"