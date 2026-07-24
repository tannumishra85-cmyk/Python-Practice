secret_code = ""


count = 0

while secret_code != "7":
    secret_code = int(input("Enter secret code "))
    count = count + 1
    if(secret_code > 7):
        print("Too high")
    elif(secret_code < 7):
        print("Too low")
    else:
        print("Correct!")
        break
print("Guess taken", count)



