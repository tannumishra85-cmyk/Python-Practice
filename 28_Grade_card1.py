def grade_card(marks):
    if(marks > 100 or marks < 0 ):
        print("Invalid number")
    elif(marks >= 90 and marks <= 100):
        print("A")
    elif(marks >=75 and marks <= 89):
        print("B")
    elif(marks >= 50 and marks <= 74):
        print("C")
    else:
        print("Fail")

num = float(input("Enter number for gradecard:"))
grade_card(num)

    