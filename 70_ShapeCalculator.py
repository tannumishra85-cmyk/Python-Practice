class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area =", 3.14*self.radius**2)        

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle Area =", self.length*self.width)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square Area =", self.side**2)        

shapes = [Circle(4), Rectangle(4,5), Square(3.5)]
for shape in shapes:
    shape.area()

