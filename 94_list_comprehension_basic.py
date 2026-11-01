numbers = [1, 2, 3, 4, 5, 6]

# [expression for item in iterable if condition]

#result = [x * x for x in numbers if x % 2 == 0]
result = [x*x if x%2== 0 else x**3 for x in numbers]


print(result)