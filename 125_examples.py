numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = {x : x**2 for x in numbers if x % 2 == 0}

print(result)

result = {x**2 for x in range(1,10) if x % 2 != 0}

print(result)

def sum_mul(a,b):
    return a+b, a*b

print(sum_mul(5,3))

text = "python is easy and python is powerful"

words = { }

for ch in text:
    words[ch] = words.get(ch, 0) + 1

print(words)