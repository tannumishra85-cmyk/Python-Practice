try:
    def add(a , b):
        return a+b
    
    def sub(a , b):
        return a-b
    
    def multiply(a, b):
        return a*b
    
    def divide(a, b):
        return a/b
    
    def remainder(a,b):
        return a%b
    


    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number : "))
    operation = input("Enter the operation you want to perfrom(+,-,*,/,%): ")
    if(operation == "+"):
        print(add(num1,num2))
    elif(operation == "-"):
        print(sub(num1,num2))
    elif(operation == "*"):
        print(multiply(num1,num2))
    elif(operation == "/"):
        print(divide(num1,num2))
    elif(operation == "%"):
        print(remainder(num1,num2))
    else:
        print("OPERATION CANNOT AVAILABLE")
        





except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Second number can't be 0.")

finally:
    print("Operation Completed.")    