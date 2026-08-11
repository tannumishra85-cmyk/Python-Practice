# **kwargs lets a function accept any number of keyword arguments.
# (named arguments)
#  Dictionary >>> **kwargs

def student(name, **marks):
    print(name)
    print(marks)

student("Tannu", math=80, python=75, database=98)