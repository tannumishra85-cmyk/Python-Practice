numbers = [10, 20, 30, 40]

# Python has an iterator for going through these values one at a time.
it = iter(numbers) # iter() >> creates iterator

print(next(it)) # gets next value
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) python raises StopIteration means no values left.
