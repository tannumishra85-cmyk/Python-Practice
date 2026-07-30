class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if(self.marks >= 90):
            print("A")
        elif(self.marks >= 75):
            print("B")
        elif(self.marks >= 60):
            print("C")
        else:
            print("D")
        

s1 = Student("Tannu", 79)
s1.grade()
