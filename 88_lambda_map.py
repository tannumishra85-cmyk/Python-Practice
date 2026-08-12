# map() >> apply this function on every item in this collection.
# map(function, iterable)  
# function >>> what operation  
# iterable >>> the collection

numbers = [1, 2, 3, 4, 5]


result = list(map(lambda x: x * 2 , numbers))

print(result)

