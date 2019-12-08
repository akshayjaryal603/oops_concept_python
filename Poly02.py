class employee():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

    def earn(self):
        print("Inside the employee class")

class childemployee1(employee):
    def earn(self):                     #Run - time polymorphism
        print("no money")

class childemployee2(employee):
    def earn(self):
        print("has money")

c = childemployee1("abc","25","12345","100,000")
c.earn()
d = childemployee2("xyz","25","12345","150,000")
d.earn()