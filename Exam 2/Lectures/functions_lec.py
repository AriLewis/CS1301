'''
function - reusable code to execute a specific task. 
'''

def greet(): #Creation of the function
    print("Hello everyone ")
    print("Welcome to ... ")

greet() #must have () or else it thinks its a variable.

def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

greet("Johnny", "Cash")

#greet() without having the augments, it is an error. 

# Positional augments also matter a lot. 

def greet(name):
    print(f"What's up {name}! ")

'''
Two types of functions:
1. Preform a task.
2. Return a value.
'''

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("John")
print(message)
print(message[1:4])

'''
review string slicing
none means the absence of a value.
'''
def greet(name):
    print(f"What's up {name}! ")

greet("David")
print(type(greet("David"))) # none type

def increment(number, by):
    return number + by

result = increment(10,5)
print(result)


'''
Keywird argument (by = 1)
positional argument (number)
'''
def increment(number, by = 1): #by = 1 is no longer positional, it is a KEYWORD ARGUMENT *****
    return number + by

result = increment(10,5)
print(result) #when there is nothing there, then it is the default value. However there is something there. 
result2 = increment(10)
print(result2)

# def increment(by = 1, number) THIS WILL BE IN EXAM 2. THE KEYWORD AUGMENT CAN NOT BE THE FIRST. IT MUST BE SECOND.

def multiply(x,y):
    return x * y

multiply(2, 3) # prints 6. 

#multiply(2, 3, 3, 5) produces an error. too many positional arguments. 

def multiply(*numbers): #STAR MAKES IT AN ARBITUATY ARGUMENT *ARGS
    print(numbers)

multiply(2, 3, 4, 5) #MAKES IT A TUPLE. 

'''
how to calculate summation or caluation of a list. WILL BE IN THE EXAM. WAS IN LAST LEC. 
'''

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number #total *= number
    return total

result = multiply(1, 2, 3)
print(result) 

'''
turned into a tuple and treated as such. Doesn't matter how many augments are passed.

1. Positiional Arguemnts
2. Keyword Arguments (increment(number, by = 1)) by = 1 is keyword
3. Arbituary Argument (*args)
4. Arbituary Keyword Arguments  (**kwargs)
'''

def save_user(**user):
    print(user)

save_user(id = 1, name = "John", age = 22) #Three keyword arguments and prints all of them. 

# THIS IS A DICTIONARY 

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2 ,3))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Spongebob", "Harold", "Squarepants")

def print_address(**kwargs):
    for value in kwargs.values():
        print(value) #prints all the values of the print_address


#**kwargs as the format of a dictionary
print_address(street = "123 Fake St.",
            city = "Atlanta",
            zip = 30303)
