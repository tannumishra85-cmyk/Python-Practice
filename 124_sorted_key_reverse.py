# Descending order---->>>  reverse= True
# sorted(data, key=function)
# sorted(data, key=function, reverse=True)


students = [
    {"name": "Tanu", "marks": 80},
    {"name": "Riya", "marks": 95},
    {"name": "Aman", "marks": 70}
]

result = sorted(students, key=lambda x: x["marks"], reverse=True)

print(result)