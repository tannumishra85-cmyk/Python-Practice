numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = {x : x * x for x in numbers if x % 2 == 0}

print(result)
