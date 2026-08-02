class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name =", self.name)


class Student(Person):
    def __init__(self, name, marks):
        self.marks = marks
        super().__init__(name)
        

    def display(self):
        print("Name =", self.name)
        print("Marks =", self.marks)


s1 = Student("Tannu",50)
s1.display()