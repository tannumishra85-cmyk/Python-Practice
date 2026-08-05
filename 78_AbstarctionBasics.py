from abc import ABC, abstractmethod # imports the tools for abstraction

class Animal(ABC): # creates an abstract class

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self): # required method
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d1 = Dog() # object creation
d1.sound()

c1 = Cat() # object creation 
c1.sound()
