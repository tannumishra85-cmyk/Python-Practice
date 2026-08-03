class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def display(self):
        print("Name =", self.name)
        print("Marks =", self.__marks)

    def update_marks(self, new_marks):
        if(new_marks >= 0 and new_marks <= 100):
            self.__marks = new_marks
        else:
            print("Invalid marks")
    def is_pass(self):
        if(self.__marks >= 40):
            print("Pass")
        else:
            print("Fail")

s1 = Student("Tannu", 80)

s1.display()
s1.update_marks(95)
s1.display()
s1.update_marks(150)
s1.is_pass()