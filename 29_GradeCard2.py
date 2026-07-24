def grade_card(num):
    
    
    if(num >= 90 and num <= 100):
        print("A")
    elif(num >=75 and num <= 89):
        print("B")
    elif(num >= 50 and num <= 74):
        print("C")
    else:
        print("Fail")


marks = [67, 78, 91, 57, 30]

for i in range(0,5):
    grade_card(marks[i])


    