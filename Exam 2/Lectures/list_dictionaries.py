'''
Prelecture notes: 

Lab may be Dictionary based. 
Next lecture will have a similar example to lab exam 2
'''
'''
List Comprehension
new_list = [ expression for item in iterable]

squares = [1, 4, 9, 16, 25]
'''

# Traditional Method 
squares = []
for x in range (1, 6):
    squares.append(x**2)

print(squares)

# List Comprehensions Method
squares = [x**2 for x in range(1, 6)]
print(squares) 

doubles = [2*x for x in range(1, 6)] #multiply by 2
print(doubles)

evens = [x for x in range(1, 11) if x%2 == 0]
print(evens)

numbers = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]
odds = [num for num in numbers if num%2 !=0]
print(odds)

words = ["    hello       ","     word     ","      Python"]
cleaned = []
for word in words:
    cleaned.append(word.strip().capitalize())

print(cleaned)

#list comprehension
cleaned = [word.strip().capitalize() for words in words]
print(cleaned)

'''
sort vs sorted list
sort() - sorts in place. Modifies the given list
sorted() = returns a new list
'''

numbers = [64, 34, 25, 12, 22, 11, 90]
numbers.sort() #Ascending order (default)
print(numbers)

numbers.sort(reverse=True) #Decending order 
print(numbers)

names = ["Zara", "Alice", "Mike", "Bob", "Charlie"]
names.sort() #Alphetical order
print(names)


#Sorted Starts 

original = [5, 2, 8, 1, 9 ,3]
result = sorted(original)

print("Original: ", original)
print("Sorted: ", result)
print("Reversed: ", sorted(original, reverse=True))

'''
Dictionaries: Ordered (Python 3.7+), Mutable, Keys must be unique, values can be anything
Keys do not have to be strings. Integers, floats, and tuples can also server as keys
'''
empty = {} 
empty = dict()

student = {"name": "Alice",
                            "age": 20,
                            "major": "Computer Science",
                            "gpa": 3.8}
print(student)

#Integer keys

squares = {1:1, 2:4, 3:9, 4:16, 5:25}

#Mixed Key types
mixed = {'a': 1, 2: 'two', (3,4): 'tuple key'}
print(mixed['a'])
print(mixed[(3,4)])

# Adding and Updating entries

students = {'name': 'Alice', 'age': 20}

#Add a new key
student['email'] = 'alice@student.gsu.edu'

print(student)

#updating an existing key
student['age'] = 21

print(student)
print(student['email'])
print(student.get('age'))

#.get() - returns None if key is not found

print(student.get('class'))

'''
The dict() Built-in Function
- Do not put quotes over the keys
- Dict uses = due to being keyword funcitons.
'''

person = dict(name = "John", age = 25, city ="New York")
print(person)
print(person.keys())
print(type(person.keys())) #dict_keys

person.update({"color" : "red"}) #.update()
print(person)

#.pop in dictionaries pass a key through the augment not a specific index like list.  

#del statement
del person['city'] #removes, does not return 
print(person)