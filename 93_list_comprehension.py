# List comprehension = create a new list using a loop in one line.

numbers = [1, 2, 3, 4, 5, 6]

squares = [n * n for n in numbers] # [expression for item in iterable]

print(squares)