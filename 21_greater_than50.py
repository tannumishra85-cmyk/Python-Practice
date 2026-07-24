marks = [ 65, 72, 38, 90, 45 ]

count = 0

for num in marks:
    if(num>50 or num == 50):  # num >= 50 also works
        count += 1


print(count)