gen = (x * 2 for x in range(1, 10) if x % 2 != 0)

print(next(gen))
print(next(gen))

for x in gen:
    print(x)