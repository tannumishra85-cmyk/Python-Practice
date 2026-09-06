# A generator expression is basically a short way to create a generator.
# similar to list comprehension creates list.

# List comprehension -----
numbers = [x * 2 for x in range(1,6)]
print(numbers)

# creates the whole list immediately.


# Generator expression------
numbers = (x * 2 for x in range(1,6))

# does not create all the values immediately. 
# It creates a generator object. 
# get values using next()

print(next(numbers))
print(next(numbers))

# ------------- WHY-----------
# memory efficeincy.
