class Student:
    def __init__(self,name , age):
        self.name = name
        self.age = age
    

    def introduce(self):
        print("Hi, I'm", self.name, " \tI'm ", self.age ," years old .")

rahul = Student("Rahul", " 20")
priya = Student("Priya", "19")

rahul.introduce()
priya.introduce()

