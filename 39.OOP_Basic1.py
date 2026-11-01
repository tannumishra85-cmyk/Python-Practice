class Student:  # class created
    def __init__(self, name): # self points to object
        self.name = name      # rahul.name = Rahul

rahul = Student("Rahul") # object_1 created
tannu = Student("Tannu") # object_2 created

print(rahul.name)
print(tannu.name)
