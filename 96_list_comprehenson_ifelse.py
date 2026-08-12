numbers = [1, 2, 3, 4, 5]

# [value_if_true if condition else value_if_false for item in iterable]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)
