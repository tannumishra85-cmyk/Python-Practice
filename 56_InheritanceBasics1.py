class Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d1 = Dog()
d1.speak()
d1.bark()