'''
While loop if uncertain how many times you have to repeat. 
'''

count = 0
while count < 5:
    print("Count is: ", count)
    count += 1

# Iterates 5 times 0-4

count = 10
while count > 0:
    print("Count is: ", count)
    count -= 5 #this repeats twice. 

''' Else on executes if nothing hits in the loop. prevents a brake. '''

# Count sum from 1 to N Examples. 
#for
total = 0
for i in range(1, 11):
    total += i
print("Sum is: ", total)

#for
numbers = [12, 50, 32, 44, 65]
total = 0
for num in numbers: 
    total += num
print("Sum is: ", total)

#while
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum is: ", total)

numbers = [1, 2, 3, 4, 5] # Calculating the product
total = 1
for num in numbers:
    total *= num
print("Total product: ", total)


''' Sentinel value - stopping at a special input'''

number = int(input("Enter a number (-1 to quit): ")) # This program ends when you type in -1. 

while number != -1:
    print("You entered: ", number)
    number = int(input("Enter a number (-1 to quit): "))
print("Goodbye!")

total = 0
number = int(input("Enter a number (0 to quit): ")) 

while number != 0:
    total += number
    number = int(input("Enter another number (0 to quit): ")) 

print("Total: ", total)

# Guessing Game

secret = 42
guess = int(input("Guess the number: "))

while guess != secret:
    if guess < secret:
        print("too low!")
    else:
        print("too high")
    guess = int(input("Guess Again: "))

print("You got it!")

#Creating functions

def greet():
    print("Hi There")
    print("Welcome aboard!")

greet()
print() # Creates an empty line. 
greet()

#greeting a certain person. 

'''first_name and last_name are arguments. While "john" and "smith" are parameters. '''
def greet(first_name, last_name):
    print(f"Hello {first_name}, {last_name}")

greet("John", "Smith")

def greet(name):
    print(f"Hello {name}")

greet("Alice")

''' 2 Types of functions:
1. Preform a task. 
2. Return a value.'''