foods = ( "Fish", "Mango", "Dahi" , "Cake" , "momos" ) 
# tuple >> collection , ordered, immutable

n_foods = list(foods)

for i in range (0,5): # Accessing element via loop
    print(foods[i])

print(foods[0]) # Accessing element 

# tuple with one element : 
# t = (5)      >>>>>>>> WRONG

t = (5 , ) # this is correct way to create tuple with one element.





# -------------------       SET   ---------------------------------------------

numbers = { 10 , 20 , 20 , 30 }

for i in numbers:
    print(i)

numbers.add(50)
numbers.remove(20)
numbers.discard(50)
deleted = numbers.pop() # return popped value also..
                        # removes random element 

#print(deleted)

#print(numbers)

# if we add a new element that already exists then it will not add >> ONLY UNIQUE ELEMENT
# can't access via index >> sets are unordered 
 
# how can we access set elements >>
# via loop
# in operator , e.g. print(20 in numbers) >> True/False
# list conversion