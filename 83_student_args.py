def student(name, *marks):
    print(name)
    print(marks)
    total = 0
    for num in marks:
        total = total + num

    print("Total =", total)


student("Tannu", 80, 75, 98)