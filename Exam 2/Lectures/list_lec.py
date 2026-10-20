'''
List: Ordered, Mutable, Indexed, Duplicates allowed, mixed types
'''

empty_list = []
scores = [95,87,73,100, 65]
mixed = [42, 'hello', True, 3.14]
print(scores[3])
print(scores[-1]) #negative indexing 
print(scores[1:4]) #list slicing - exlusive

shopping = ['milk', 'eggs', 'bread']
shopping.append("butter")
shopping.append("cheese") # append adds to the end of the list. 
print(shopping)

'''
insert(): inserts an element at a specific position. Takes two arguments:
    1. the index and the value to the insert.
'''

colors = ['red','green', 'blue']
colors.insert(1, 'yellow') #inserts yellow at index 1. 

print(colors)

colors.insert(0, "white") # inserts at the begining
print(colors)

'''
extend() : Adds all elements from another interable (list,tuple, etc.) to the end of the list. 

Unlike append(), which adds the entire list as a single element, extend() function MERGES the elemments.

Extend has to pass an interable object
append adds at the end of the list as a single identity. 
'''

team_a = ["Alice", "Bob", "carol"]
team_b = ["Dave", "Eve"]

team_a.extend(team_b) #extend merges elements

print(team_a)

team_c = ["Frank", "grace"]

team_c.append(team_b) #ccreates a list within a list
print(team_c)
print(len(team_c))

fruits = ["Apple", "Banana", "cherry"]
fruits.extend("mango")
print(len(fruits))
print(fruits) #counts the characters, not the entire word. 

fruits.append("kiwi") # only adds whole thing not just the characters.
print(fruits)
print(len(fruits))

scores = [95, 87, 100]
scores.append(75)
#scores.extend(34) can not extend on integers. 
print(scores)

'''
    APPEND VS EXTEND ON THE EXAM
'''

scores = [95,87,100]
fruits = ["apple", "grape", "banana"]
new_list1 = scores + fruits
print(new_list1)

new_list2 = fruits + scores
print(new_list2)

animals = ["cat", "dog", "bird", "dog", "fish"]
animals.remove("dog") # only removes the first dog 
# value error if not in list 
print(animals)

if 'lion' in animals: # non error way
    animals.remove("lion")
else:
    print('lion not in the list')
print(animals)

tasks = ["write report", "send email", "attend meeting", "update docs"]

last_task = tasks.pop()
print("Removed: ", last_task)
print("remaining: ", tasks)

send_task = tasks.pop(1)
print("removed: ", send_task)
print("remaining: ", tasks)

numbers = [10,20,30,40,50,60]

#Delete element at index 2.
del numbers[2]
print(numbers)

# Delete a slice(elements at index 1 through 2)
del numbers[1:3]
print(numbers)

fruits = ["apple", "banana", "cherry", "grapes"]
for fruits in fruits:
    print(fruits)

#enumerate(): when you need both index and the value of each element.
students = ["dave", 'alice','bob','carol']

for index, name in enumerate(students):
    print(f"{index+1}.{name}")

students = ["dave", 'alice','bob','carol']
for index, name in enumerate(students, start=1):
    print(f"Student #{index}:{name}")


'''
Nested List: A 3x3 matrix as a nested list.
How to access entire row? 
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0]) # gives first row
print(len(matrix)) # three because three rows. 

#Access a single element
print(matrix[0][1]) # prints 3
print(matrix[2][0]) # prints 7

prices = [10.0, 25.5, 8.0, 42.0, 15.75]
#Apply 10% discount to all prices

for i in range(len(prices)):
    prices[i] = prices[i]*0.9

print(prices)


numbers = [3, -1, 7, -4, 0, 9, -2, 5]
#Collect positve numbers into new list
positive = []
for num in numbers:
    if num > 0:
        positive.append(num)
print(positive)

'''
avoid modifying a list while iterating over it. ***
'''


#Wrong approach to modifying list
scores = [55, 40, 82, 48, 91, 60, 37, 74]
for score in scores:
    if score < 60:
        scores.remove(score)
print(scores)

# if element is added after the first iteration, it will be skipped. i.e. 40 in above list. 


#correct way
scores = [55, 40, 82, 48, 91, 60, 37, 74]
for score in scores[:]: #created a copy here
    if score < 60:
        scores.remove(score)
print(scores)

'''
List Comprehension: the proper syntax
new_list =[expression for item in iterable] 

original = [ 1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

- Traditional for loop to get squares. 
'''

squares = []
for x in range(1,6):
    squares.append(x**2)
print(squares)

# List COmprehension
squares = [x**2 for x in range(1, 6)]
print(squares)