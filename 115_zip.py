# zip ... combines corresponding elements 
# syntax >> zip(iterable1, iterable2)
# zip itself produces a zip object (iterator)

names = ["Tannu", "Bhumi", "Suchi", "Ruchi"]
marks = [10, 20, 30]

result = list(zip(names, marks))
print(result)

# zip() stops when the shortest itrable runs out.
# so, ruchi has no partner and isn't included.
