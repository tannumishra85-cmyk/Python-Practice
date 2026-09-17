# any() → at least ONE is True
# all() → EVERY ONE is True

numbers = [2, 4, 7, 8]

print(any(x % 2 != 0 for x in numbers)) # True
print(all(x % 2 == 0 for x in numbers))# False

# any can stop as soon as it finds one true.
# all can stop at first false.


