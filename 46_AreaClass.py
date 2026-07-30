class Area:
    def Rectangle(self,length, width):
        print("Area of rectangle =", length*width)

    def Square(self, side):
        print("Area of square =", side**2)

    def Circle(self, radius):
        print("Area of circle =", 3.14*radius*radius)



r1 = Area()
r1.Rectangle(12, 9)
r1.Square(20)
r1.Circle(3)
