age = 20
if age >= 18: #boolean type
    print("You can vote")
    print("You are an adult")
    print("Have have full legal rights") #because they are tabed, they belong to the if statement. 

is_logged_in = True
if is_logged_in:
    print("Welcome Back!")

a = 50
b = 50
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print('Grade C')
elif score >= 60:
    print("Grade D") #executes only the first one that is true. 

age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday") # can repreat this up to sunday 
print("Done@!!")

a = 200
b = 50
if b > a:
    print("b is greater than a")
elif a == b:
    print(" a and be are equal ")
else:
    print("a is greater than b")

a = 500
b = 50

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a") # provides default action when none of the other are true. Should be last.

''' Coding Question in class'''

num = int(input("Please enter an integer:"))

if num % 2 == 0: # remember module of 2 must be 0 for even. Depends on the right most digit. if its odd, then the number is odd. 
    print("Even")
elif num % 2 > 0:
    print("odd")


tempeture = 22

if tempeture > 30:
    print("It's hot outside")
elif tempeture > 20:
    print("It's warm outside")
elif tempeture > 10:
    print("its cold outside")
else:
    print("it's cold outside.")

username = input("Enter Username")

if len(username) > 0:
    print(f'Welcome, {username}!')
else: #useful for error handling. 
    print("ErrorL Username cannot be empty.")

# Short hand if

a = 5
b = 2
if a > b: print("a is greater than b")

# short hand If...else

a = 10
b = 60
print("A") if a > b else print("B")

a = 100
b = 40
c = 500

if a > b or a > c:
    print("At least one of the conditions is true.")

a = 50
b = 200
if not a > b:
    print("a is NOT greater than b")

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount Applies")

'''Nested if statement '''
x = 40

if x > 10:
    print("Above 10,")
    if x > 20:
        print("and also above 20")
    else:
        print(" but not above 20.")