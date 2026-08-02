class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Dog barking")


class Cat(Animal):

    pass


d = Dog()
c = Cat()

d.speak()
c.speak()