'''
---
Exam 2 Review: Loops, Functions, Strings, List, and Dictionaries
---
What has been told will be on exam: 
- append vs extend
- avoid modifying a list while iterating over it
- split and join

# General Review Notes
## Loops
- for loop
- while loop
- nested loop
- break
- else
- continue

## Functions
- positional arguments
- keyword arguments
- *args
- **kwargs
- scope of a variable
- global keyword

## Strings
- slicing
- lower() upper()
- title()
- strip()
- split()
- join()
- find()
- count()
- replace ()

## List
 sort(), sorted()


## Dictionaries
- adding and updating entries
- accessing values
- get(), keys(), values(), items(), update(), pop(), popitem(), nested dictionary '''


# List

'''
Negative Indexing: starts backwards at 1, not zero. 
List Slicing: exlusive
'''

from codecs import StreamWriter


list = [95, 87, 73, 100, 65]
print(list[-1]) #Gives [65]

print(list[1:4]) #Gives [87, 73, 100]

'''
append(): Adds to the end of the list
    - single identity
    - creates a list within a list
insert(): Requires the index and the value of the insert. 
extend(): Adds all elements from another interable (list, tuple,etc.) to the end of the list.
    -must pass an interable object
    - MERGES the elements. 
    - CAN NOT EXTEND ON INTEGERS. 
'''

shopping = ['milk', 'eggs', 'bread']
shopping.append('butter') #['milk', 'eggs', 'bread', 'butter']
print(shopping)

shopping.insert(1, 'noodles') #[milk, noodles, eggs, bread]
print(shopping)

team_a = ['Alice', 'Bob', 'Carol']
team_b = ['Dave', 'Eve']

team_a.extend(team_b) # ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']
print(team_a)

'''
append(), extend() with len()
'''
team_c = ['Trey', 'Ari']

team_c.append(team_b) 
print(team_c) #['Trey', 'Ari', ['Dave', 'Eve']]
print(len(team_c)) # 3

team_c.extend('kate') # ADDS EACH LETTER INDIVIDUALLY INTO THE LIST
print(team_c)  #['Trey', 'Ari', ['Dave', 'Eve'], 'k', 'a', 't', 'e']
print(len(team_c)) # 7 

score = [97, 87, 65]
score.append(76)
#score.extend(76) gives error
print(score)

'''
.pop() vs .remove()

.remove(): can produce an error if not in a for-else loop
'''

animals = ['cat', 'dog', 'fish', 'dog' 'rabbit']

animals.remove('dog') # only removes the first dog. 
#animals.remove('lion') error
print(animals)

# A way of using .remove() without an error. 
if 'lion' in animals:
    animals.remove('lion')
else:
    print('Lion is not in the list')
print(animals)

tasks = ["write report", "send email", "attend meeting", "update docs"]

last_task = tasks.pop() #Removes the list one on the list

send_task = tasks.pop(1) #removes index 1
print("removed:", send_task)
print('remaining:', tasks)

'''
del and enumerate()

enumerate(): when you need both index and the value of each element.
1. dave
2, alice
3, bob
4, carol

'''
numbers = [10,20,30,40,50,60]

del numbers[1:3] #deletes 20,30
print(numbers)

students = ["dave", 'alice','bob','carol']

for index, name in enumerate[str](students):
    print(f"{index+1}, {name}")

'''
Nested List: A 3x3 matrix example. 
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0]) #gives first row
print(len(matrix)) #3 because 3 rows

#Accessing a single element

print(matrix[0][1]) # Row 1, index 1. prints 2

# For if 

numbers = [3, -1, 7, -4, 0, 9, -2, 5]
#Collect positve numbers into new list
positive = []
for num in numbers:
    if num > 0:
        positive.append(num)
print(positive)

'''
No modifying a list while iterating over it *** 
'''

#Correct way of doing this

scores = [55, 40, 82, 48, 91, 60, 37, 74]
for score in scores[:]: #Creates a copy here
    if score < 60:
        scores.remove(score)
print(scores)

'''
List Comprehension: traditional for list to get squares
'''
squares = []
for x in range(1,6):
    squares.append(x**2)
    print(squares)

#List Comprehension Example

squares = [x**2 for x in range(1, 6)]
print(squares)

# Functions

'''
Type of Arguments
1. Positional Arguments
2. Keyword Arguments ===============> (by = 1)
3. Arbitrary Arguments =============> (*args) -------- tuple
4. Arbituary keyword Arguments =====> (**kwargs) ----- Dictionary
'''

# .items is the only way to get both key and value
def print_address(**kwargs):
    for key, value in kwargs.items(): # NOTE the difference here with .items and .value
        print(f"{key}: {value}")
    
print_address(street = "1 Park Place",
            city = "Atlanta",
            state = "GA",
            zip = "30303"
)


# Example two

def shipping_label(*args, **kwargs): # Args should always come first when passing args and kwargs at the same time. 
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value)

shipping_label("Spongebob", "squarepants", "Harold",
                street = "Petit Science",
                city = "atlanta",
                state = "GA",
                zip = 30303) #make sure to pass arbituary and kwarg

print()

# Important Algorithm

def get_evens(numbers): 
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

my_list = [1,2,3,4,5,6,7,8]
print(get_evens(my_list))

def word_freq(sentence):
    freq = {} #empty dic
    words = sentence.split() #splits each character by wide space.
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

result = word_freq("the cat sat on the mat the cat")
print(result) # the: 3 cat: 2 sat: 1 on:1 mat: 1


'''
Introduction to Scope
1. Local Scope: a variable created INSIDE a function belongs to the local scope of that funciton.
2. Global Scope: a variable created in the main body Python code is a global variable and belongs to the global scope.
    - if you need to create, but are stuck in local, you can ue global keyword
'''

def myfunc():
    x = 300 #available to any function within the function.
    def myinnerfunc():
        print(x)
    myinnerfunc()

'''
Global Keyword, 
if there is another global, it can change it. 
'''
#example
x = 80
def myfunc():
    global x #global variable
    x = 200

myfunc()
print(x)

'''
Naming Variable
if you operate with the same variable name inside and outside of the function, Python will treat them as two seperate variables,
one available in the global scope (outside func) and one vailable in the local scope. (inside func)
'''

count = 0
def increment():
    global count #grabs from the global count = 0
    count += 1
    print("Inside function: ", count)

increment()


'''
Strings:
Do we have negative steps? yes it goes backwards
'''

letters = "ABCDEfgHIJK"
print(letters[-1]) # K.
print(letters[1::5]) #bg
print(letters[:4]) #ABCD exlusive
print(letters[::]) #everyhing
print(letters[::-1]) #everything backwards


#NOTE: this will be on the exam

def is_palindrom(word):
    if word[::] == word[::-1]:
        return True
    else:
        return False

print(is_palindrom("racecar")) #True
print(is_palindrom("book")) #False 

def is_pal(word):
    return word [::] == word[::-1] # SHORTED WAY OF TYPING THE PREVIOUS FUNCTION

print(is_pal("racecar"))

'''
Upper(), lower(), title(), capitalize()

.upper() - makes all the letters uppercase
.lower() - makes all the letters lowercase.
.title() - Capitalize first letter of every word
.capitalize() - Capitalizes only the first letter and rest lower case. 
'''

name = 'hello, world!'
print(name.upper()) # all uppercase
print(name.lower()) # all lower case

sentence = "the Quick Brown Fox"
word = "pYTHON"

print(sentence.capitalize()) # first letter captalized, rest lower
print(word.capitalize())

book = "the lord of the rings"
print(book.title()) #first letter of every word is capitalized.


'''
Searching inside string: find() ===> returns the index of the first occurence of a substring.
'''

text = "I love python and python loves me"
print(text.find("Python")) # Returns 7
print(text.find("Java")) #prints -1 if not in the string.

print(text.find("Python", 10)) #Search  from index 10 to that substring. prints 18


'''
replace()
strip()
'''

text = "I like cats. Cats are great."
print(text.replace("Cats", "dogs")) #replace(old, new)

user_input = "           hello world        "
print(user_input.strip()) #removes whitesplaces

