class Animal:

    def __init__(self):
        self.type = "Animal"


class Dog(Animal):

    def __init__(self):
        self.type = "Dog"
        super().__init__() # Here Parent overwrite the self.type


d = Dog()

print(d.type)