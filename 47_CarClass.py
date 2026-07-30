class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 10

    def brake(self):
        self.speed = self.speed - 10

    def display(self):
        print("Brand =", self.brand)
        print("Speed =", self.speed)

car = Car("Toyota" , 50)
car.accelerate()
car.display()
car.brake()
car.display()
        