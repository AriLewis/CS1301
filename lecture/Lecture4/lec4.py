x = 7
print(id(x))
# name of the variable is x. ID is the exact location of the variable in the memory. 

x = 6
del x # here x would be garbage collected.

x = 704536 # any singular digit can not be changed therefore immutable. 

print(2**3) #exponent

print(19/4) #division is always a float number ! 
print(18//4) #this is floor division. GIVES US AN INTEGER

print(18/4)
print(18//4)
print(-18/4)
print(-18//4) #just explaining floor division more.

print(23/10)
print(23 % 10) #Mod Prints remainder of division.  Always gives the right most digit.
print(-25 % 4)

print(25 % 2) # odd numbers always 1 for mod 2. 
print(26 % 2) # even always gives 0 for mod 2


import math
number = 49
print(math.sqrt(49)) #has to use the import statement here to use the module. Name of module followed by a dot. 

number = 4.85
print(math.ceil(number)) # Rounds up and prints 5
print(math.floor(number)) # Rounds down and prints 4

print(math.pow(3, 2)) # 3 to the power of 2 3^2. 

import random
print(random.randrange(3)) # 0 to 2, does not include 3. 0,1,2 is possible.
print(random.randrange(6)) # 0-5 range. 
print(random.randrange(10, 21)) # from 10-20

print(random.randint(1, 99)) #randint INCLUDES 99. 

print(random.random()) #generates from 0-1, 1 excluded. 
 
