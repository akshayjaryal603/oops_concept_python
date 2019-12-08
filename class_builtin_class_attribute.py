class Employee:
    "Common base class for all employees"
    empCount = 0        #class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        #Employee.empCount += 1

    # def displayCount(self):
    #     print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : %s Salary: %d"%(self.name , self.salary))

emp1  = Employee("Akshay",800000000)
#emp2 = Employee("Rajat", 1090000000)
#emp3 = Employee("Vikram", 2090000000)
#emp1.displayCount()
emp1.displayEmployee()
#emp2.displayEmployee()

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)