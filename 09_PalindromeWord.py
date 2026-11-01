name = "Tannu"
print(name[2])
#Accessing elements using their index value..

print(name[-3])
# Positive index → Left to Right
# Negative index → Right to Left

word = input("Enter your words ")

print("sliced part of string : ", word[6:11]) # [start : end]
print("jumped string : ", word[0:7:2]) # [start : end : step]
print("Reverse:",word[-1::-1]) # [start = -1  : end : step = -1]
