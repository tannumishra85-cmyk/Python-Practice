numbers = [3, 8, 12, 17, 20, 25, 30]

# using filter + lambda
result = list(filter(lambda x : x > 10 and x % 2 == 0, numbers))

print(result)


# Or, 

# using list comprehension
result = [x for x in numbers if x > 10 and x % 2 == 0] 

print(result)