# import calculator # for full module
#  then we have to use ->> print(calculator.add(10, 20))

#from calculator import add, multiply
# In this case you just have to import function that you need.

# We can also write from calculator import multiply as mul

import math # math Module ->> Python's standard-library module
import calculator as calc 
import random

# calculator -> Original module name
# calc ->> alias/nickname

print("Sum =", calc.add(10, 20))
print("Multiply =",calc.multiply(2, 50))
print(calc.add(23, 23))

print("")
print(math.sqrt(25)) # sqrt ->> function inside math
print(math.pi) # pi ->> varible/value 
print(math.pow(2,3)) # Power ->> 2^3 = 8.0
print(math.ceil(4.2)) # ceil() moves to the whole number ABOVE it on the number line.
print(math.ceil(-2.2)) # return -2 nearest ( up ) number.
print(math.floor(4.7)) # floor() means go DOWN to the whole number below it
print(math.factorial(5))
print(math.gcd(12,15)) # Greatest Common Divisor
# math function return floating-point numbers

print(" ")
print(random.randint(1,10)) # returns random numbers between [a, b]

