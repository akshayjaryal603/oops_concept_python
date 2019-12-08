class employee1():
    def name(self):

        print("Harshit is his name")


def salary(self):
    print("3000 is his salary")


def age(self):
    print("22 is his age")


class employee2():
    def name(self):
        print("Rahul is his name")


def salary(self):
    print("4000 is his salary")


def age(self):
    print("23 is his age")


def func(obj):
#Method Overloading
    obj.name()
    obj.salary()
    obj.age()

obj_emp1 = employee1()
obj_emp2 = employee2()

func(obj_emp1)
func(obj_emp2)