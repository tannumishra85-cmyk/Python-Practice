class Dog:
    def speak(self):
        print("Dog barks")


class Cat:
    def speak(self):
        print("Cat meows")

d1 = Dog()
c1 = Cat()

animals = [d1 , c1] # That's Polymorphism 🔥

for animal in animals:
    animal.speak()
