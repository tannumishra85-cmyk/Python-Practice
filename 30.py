def grade_card(num):
    if(num >= 90 and num <= 100):
        return "A"
    elif(num >=75 and num <= 89):
        return "B"
    elif(num >= 50 and num <= 74):
        return "C"
    else:
        return "Fail"


marks = [67, 78, 91, 57, 30]

for i in range(0,5):
    print(marks[i], ":" ,grade_card(marks[i]))

marks.sort()
print("Heighest :", marks[4])
print("Lowest :", marks[0])