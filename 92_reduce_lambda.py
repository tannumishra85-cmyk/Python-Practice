# reduce() >> many values → reduce → one value
# reduce come from the functools module 
from functools import reduce

numbers = [10, 20, 30, 40, 50]

result = reduce(lambda a,b : a + b , numbers) 

print(result)


# map()    → many results → map object → list(...) often used
# filter() → selected results → filter object → list(...) often used
# reduce() → ONE final result → no list needed