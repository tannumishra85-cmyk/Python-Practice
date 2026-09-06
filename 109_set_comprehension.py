# Set comprehension >> {It removes duplicates}

# {x * 2 for x in numbers}

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

result = {x**2 for x in numbers if x % 2 != 0}

print(result)