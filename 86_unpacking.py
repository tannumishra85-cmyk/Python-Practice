def add(a,b,c):
    return a + b + c

numbers = (10, 20, 30)

print(add(*numbers)) 
# "*" also opens/unpacks the tuples into separate positional arguments.


# *args while defining

#        ↓
#    COLLECT
# 10,20,30 → (10,20,30)

# *numbers while calling
#        ↓
#     UNPACK
#(10,20,30) → 10,20,30


# --------------Another example-----

def student(name, course):
    print(name, course)

details = {"name": "Tannu", "course": "MCA"}

student(**details)

# * while defining     → collect positional → tuple
# ** while defining    → collect keyword   → dictionary

# * while calling      → unpack tuple/list → positional arguments
# ** while calling     → unpack dictionary → keyword arguments

# ------------Another example-----------------
def address(name, age):
    print(name , age)

info = ("Tannu", 21)

address(*info) # unpacking dictionary >> keyword arguments
