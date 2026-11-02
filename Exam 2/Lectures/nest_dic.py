'''
Lecture 10: 
'''
# Iterating over a dictionary
prices = {'coffee': 3.5, 'tea': 2.0, 'juice':4.5}

for items in prices: # same as: for items in prices.keys()
    print(items)

for key in prices.keys():
    print(key)

# Iterating over the values
for value in prices.values():
    print(f"{value:.2f}")

# Iterating over key-value pairs with .items()
for item, prices in prices.items():
    print(f"{item:10s} ${prices:.2f}") # 10s means 10 spaces, s means string, f means float

'''
Dictionary Comprehension
Syntax ==> {key_expr:value_expr for item in interable}
       ===> {key:value for key, value in iterable}
'''

# Squares = {1:1, 2:4, 3:9,...}
squares = {n:n**2 for n in range(1,6)}
print(squares) 

words = ['apple', 'banana', 'cherry']
word_lengths = {word:len(word) for word in words}
print(word_lengths)

# Celcius to Fahrenheit
celcius = [0, 20, 37, 100]
to_fahrenheit = {c: (c * 9/5) + 32 for c in celcius}
print(to_fahrenheit)


# Nested Dictionary
myfamily = {
    "child1": {
        "name": "John",
        "year": 2004
    },
    "child2": {
        "name": "Jane",
        "year": 2007
    },
    "child3": {
        "name": "Jim",
        "year": 2011
    }
}
print(len(myfamily)) 
print(myfamily["child1"])
print(myfamily["child2"]["name"])

school = {
    'Alice': {
        'age': 18,
        'grades':{'math': 95, 'english': 90}
    },
    'Bob': {
        'age': 20,
        'grades':{'math': 85, 'english': 80}
    },
    'Charlie': {
        'age': 22,
        'grades':{'math': 75, 'english': 70}
    }
}
# Get Alice's age
print(school['Alice']['age'])
# Get Bob's math grade
print(school['Bob']['grades']['math'])
# Get Charlie's english grade
print(school['Charlie']['grades']['english'])

# Get all students' ages
for student in school:
    print(student, school[student]['age'])

# Get all students' grades

# Scrabble Points Dictionary

points = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}
print(points)

# THIS WILL BE ON THE EXAM
word = input("Please enter a word:").upper()
total_points = 0
for letter in word:
    total_points += points[letter]
print(f"The total points for {word} is {total_points}")

prices = {'coffee': 3.5, 'tea': 2.0, 'juice':4.5}
prices.popitem()
print(prices)
