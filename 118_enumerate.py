# zip() >> combines corresponding values 
# enumerate() >> gives index + value 


fruits = ['Apple', "Banana" , "Mango"]

for index, fruit in enumerate(fruits, start=1):
    # here start= 1 tells enumerate  start from index 1 .
    print(index, fruit)

# internally enumerate produces >>
# (0, 'Apple') 
# through loop >>  index is 0 and fruit is Apple

# for index, value in enumerate(iterable)

# zip()       → combines separate iterables
# enumerate() → adds an index to one iterable