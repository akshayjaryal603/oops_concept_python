
class Animal:
    def speak(self):
        print("speaking")

class Dog(Animal):
    def speak(self):
        print("Barking")

c1 = Dog()
c1.speak()
