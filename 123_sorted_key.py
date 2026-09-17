students = [
    {"name" : "Tannu" , "marks" : 80},
    {"name" : "Riya" , "marks" : 90},
    {"name" : "Sonii" , "marks" : 89}
]

result = sorted(students, key=lambda x : x["marks"])
# Entire dictionary are returned but python uses "marks" to decide their order.


print(result)