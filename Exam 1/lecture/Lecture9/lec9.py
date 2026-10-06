temperature = 25
is_raining = False
is_weekend = True
if(temperature > 20 and not is_raining) or is_weekend:
    print("Great Day for outdoor activies")

age = int(input("Enter your age: "))
has_license = False
if age >= 18:
    if has_license:
        print("you can drive")
    else: 
        print("You need a license")
else: 
    print("You are too young to drive.")    # question: What would be the output?

''' Start of loops '''

for i in [1, 2, 3 ,4, 5]:
    print(i)

students = ["Alice", "Bob", "Charlie", "Diana"]
for students in students:
    print(f"Hello, {students}")

word = "Python"
for w in word:
    print(w, end=" ")


''' Membership operators: in/not in'''

barcelona_fc_roster = ["Messi", "Lamine", "Olmo", "Raphina"]
name = input("Enter a name to check: ")
if name in barcelona_fc_roster:
    print(f"Found {name} on the roster")
else:
    print(f"could not find {name} on the roster.")

arcelona_fc_roster = ["Messi", "Lamine", "Olmo", "Raphina"]
name = input("Enter a name to check: ")

if name not in barcelona_fc_roster:
    print(f"Could not find {name} on the roster")
else:
    print(f"Found {name} on the roster")


# Iterate over keys of the dictionary 
student_grades = {
    "Alice":95,
    "bob":87,
    "Charlie": 92
}

for name in student_grades:
    print(f"{name}: {student_grades[name]}")

for i in range(5):
    print(i) # prints 0-4. This is a way of counting. 

'''
range(stop) ==> 0 to stop -1
range(start, stop) ==> start to stop -1
range(start,stop,step) ==> start to stop -1, incrementing steps
'''

for i in range(1, 11, 2): # 1, 3, 5, 7,9
    print(i, end=" ")

for i in range(1, 11, 3): # 1,4,7,10
    print(i, end=" ")

for i in range(10, 0, -1): #prints in decending order
    print(i, end=" ")

# range with list indexing
fruits = ["apple", "banana", "cherry", "grapes"]

for i in range(len(fruits)):
    print(f"Item {i}: {fruits[i]}")

x = 7
if x > 5:
    if x< 10:
        print("Branch 1")
    else:
        print("Branch 2")
else:
    print("Branch 3")

for i in range(20,4,-4):
    print(i)