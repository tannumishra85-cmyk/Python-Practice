names = ["A", "B", "C"]
marks = [80, 70, 40]

for name,mark in zip(names, marks):
    if mark >= 50:
        print(name , mark, "pass")
    else:
        print(name, mark,  "Fail")

