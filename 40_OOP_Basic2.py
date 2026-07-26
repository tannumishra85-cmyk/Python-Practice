class Student:

    def __init__(self, name):
        self.name = name

rahul = Student("Rahul")
# priya a variable also pointing the same object(rahul.name)
priya = rahul

priya.name = "Anu"
# This line changed the object that both variables point to.

print(rahul.name)
print(priya.name)

#Output :-
#Anu
#Anu
