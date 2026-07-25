def grade_card(num):
    if(num >= 90 and num <= 100):
        return "A"
    elif(num >=75 and num <= 89):
        return "B"
    elif(num >= 50 and num <= 74):
        return "C"
    else:
        return "Fail"

 
students = {
    "Tannu" : 100 ,
    "Anu" : 99 ,
    "Rahul" : 89
}

for name, mark in students.items():
    print(name , " : " , mark , " : " , grade_card(mark) )



