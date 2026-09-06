names = ['A', "B", "C"]
marks = [80, 40, 90]

result = [name for name, mark in zip(names, marks) if mark >= 50]

print(result)