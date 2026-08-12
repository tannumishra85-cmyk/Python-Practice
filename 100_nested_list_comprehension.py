numbers = [[10, 20], [30, 40], [50, 60]]

result = [x for row in numbers for x in row] 
# two nested loops in one line

print(result)