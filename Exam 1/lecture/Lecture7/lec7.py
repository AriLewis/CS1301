student = {"name": "Maria",
                                         "age": 18,
                                        "gpa": 3.38} # keys to dictionary

print(student["age"]) # access entries in dictionary
student["email"] = "maria@student" # how to add new entry to dictionary
print(student)
del student["gpa"]
print(student)

email = student.pop("email") # pop can return and delete. 
print(email)
print(student)
'''
Equals: a == b. 
Not Equal: a != b 
Less than: a < b
less than r equal: a <= b
Greather than or equal: a >= b
'''

a = 30
b = 200
if b > a:
    print("b is greater than a") 

number = 15
if number > 0:
    print("the number is positive")

a = 50
b = 100
if b > a: #must indent or gives indentation error
    print("b is greter than a")

age = 17
if age > 18:
    print("u r an adult")
    print("u can vote")
    print("you have full legal rights") # all of the tabs belong to the if statement
print("u can't vote") # Does not belong to the if state 
