marks = [70, 80, 90]
total = 0
count = 0
for mark in marks:
    print(mark)
    total = total + mark 
    count = count + 1

print("Total =", total)
print("Average =", total/count)