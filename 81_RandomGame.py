import random
names = ["Tannu", "Aditya", "Lucky"]
print(random.choice(names))


random.shuffle(names)
print(names)
# choice is a valid function in random module.
# random.randint ->> random integer in given range will be printed 
# random.choice ->> random number/text printed
# random.suffle ->> randomly reaaranges the list (changes the og list)

print(random.random()) 
# returns random decimal number from 0 up to (but not including) 1

print(random.uniform(5, 7))
# returns random floating point number in given range