# generators >> is a simple way to create an iterator using yeild.
# return >> gives a value and ENDS the function
# yield >> gives a value and PAUSES the function.

def numbers():
    yield 10 # yield instead of return 
    yield 20 
    yield 30

gen = numbers()

print(next(gen))
print(next(gen))

# Why? Generators:-

# if we need numbers from 1 to 1 lakh a normal list [1, 2, 3, ..., 100000] A generator 