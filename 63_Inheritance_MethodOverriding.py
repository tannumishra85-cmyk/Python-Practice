class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand =", self.brand)

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed

    def display(self):
        print("Speed =", self.speed)
        print("Brand =", self.brand)


c1 = Car("Toyota" , 120)
c1.display()
