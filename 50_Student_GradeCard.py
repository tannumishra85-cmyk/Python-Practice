class Student:
    def __init__(self, name):
        self.name = name 
        self.marks = []

    def add_marks(self,marks):
        self.marks.append(marks)


    def average(self):
        count = 0
        total = 0
        for i in self.marks:
            total = total + i
            count = count + 1

        print("Average =", total/count) 

    def display(self):
        print("Name =", self.name)
        for i in self.marks:
            print(i)

s1 = Student("Tannu")
s1.add_marks(79)
s1.add_marks(81)
s1.display()
s1.average()


    