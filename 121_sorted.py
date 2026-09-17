# sorted creates a new sorted list.
# By default, Python sorts in ascending order.
# key= tells use this particular property/value while sorting order.

words = ['apple', 'hi', 'cat' , 'banana']

result = sorted(words, key= len)
# it sorts according to length...

print(result)