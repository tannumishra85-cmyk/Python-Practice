marks = [70, 80, 30, 90 , 50]

highest = marks[0]
lowest = marks[0]

count = 0
for i in range(len(marks)):
    if(marks[i] > highest):
        highest = marks[i]

    if(marks[i] > 60):
        count = count + 1


print(highest)
print(count)


for mark in marks:
    if(lowest > mark):
        lowest = mark


print(lowest)
    