class employee():
    def __init__(self, name, age, id, salary):      #creating a function

        self.name = name                                # self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id
    def show(self):
        print("name is:", self.name)
        print("age is:", self.age)
        print("salary is:", self.id)
        print("Id is:", self.id)

emp1 = employee("abhishek", 22, 1000, 1234) # creating objects

emp2 = employee("arjun", 23, 2000, 2234)

print(emp1.__dict__)
#Prints dictionary

emp1.show()
print(emp2.__dict__)
emp2.show()
