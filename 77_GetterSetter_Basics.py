class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self): # Getter (Programmers design classes)
        return self.__marks


    def set_marks(self, new_marks): # setter 
        if(0 <= new_marks <= 100):
            self.__marks = new_marks
        else:
            print("Invalid marks")

    def display(self):
        print("Name =", self.name)
        print("Marks =", self.__marks)
        
    def is_pass(self):
        if(self.__marks >= 40):
            print("Pass")
        else:
            print("Fail")

s1 = Student("Tannu", 80)

print(s1.get_marks()) # In normal code we'd use 

s1.set_marks(95)
print(s1.get_marks())

s1.set_marks(150)

s1.display()
s1.is_pass()

print(s1._Student__marks) # using Python's mangled name.
        