def calculate_avg(marks):
    total = 0
    for i in marks:
        total = total + i

    avg = total / len(marks)
    return avg



marks = [65, 72, 38, 90, 45]
print(calculate_avg(marks))