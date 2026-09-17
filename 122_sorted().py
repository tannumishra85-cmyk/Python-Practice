words = ['apple', 'hi' , 'banana' , 'cat']

result = sorted(words, key=lambda x : len(x))
# for each item, calculate its length and use that length for sorting...
# key doesn't change the items


print(result)
