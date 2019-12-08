class CSStudent:        # class
    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll):
        # Instance Variable
        self.roll = roll

    # Retrieves instance variable
    def getAddress(self):
        return self.address

    # Adds an instance variable
    def setAddress(self, address):      # User Defined Method
        self.address = address

# Main Code
std = CSStudent(101)
std.setAddress("Delhi")
print(std.getAddress())
print(CSStudent.stream)


