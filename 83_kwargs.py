# Let's a function accept any number of keyword arguments (named arguments)

def show(name, **marks):
    for subject,mark in marks.items():
        print(subject, "=", mark)

# *args >> tuple 
# **kwargs >> dictionary  >> we can use dictionary methods 

# *args >> unnamed/positional values >>>>>> tuple
# **kwargs >> named/keyword values >>>>>> dictionary 
# kwargs >> key-word arguments


show(
    "Tannu",
    math = 80,
    python = 75,
    database = 98

)


# def function(normal_parameters, *args, **kwargs) is a natural structure.
show("Tannu", math=80, python=75, database=98)
