# List comprehension
# [x * x for x in numbers]

# Dictionary comprehension
# {x: x * x for x in numbers}

# list >> value 
# Dictionary >> key : value


numbers = [1, 2, 3, 4, 5]

# {key: value for item in iterable}
result = {x : x * x for x in numbers}

print(result)