"""This is review from last week"""
import random #review for last week

number = random.random() #prints any number between 0-9
print(number) 
print(f"{number:.2f}") # two decimals

number1 = random.randrange(10)
print(number1) #10 is exlusive. 10 is the ARGUMENT

num2 = random.randrange(10, 20) #10-20 exlusive. 
print(num2)

num3 = random.randint(1, 100) # 1-100 inclusive
print(num3)

import math
radius = float(input("Enter radius of a circle: "))
area = radius * radius *math.pi
print(f"Area of the circle is {area:.2f} m^2 ")

name = "Ari"
print(type(name)) # prints the variable type - str
print(len(name)) # Gives how many characters are in the lenght of the string (3)

message = "Hello World"
print(len(message)) # 11 characters due to the space.

city = "ATLANTA"
print(len(city))
print(city[1]) #Prints the second character. Refers to the INDEX. Length of string minus 1 for final letter. 

# print(len(city[7])) String index out of range.city

my_string = "Hi class. Welcome to this club!"
print(len(my_string))
print(my_string[30])

str1 = "hello"
str2 = "Everyone"
str3 = str1 + str2 #String concatinate. Join together strings with no wide space
print(str3)

str4 = str1 +  " " + str2
print(str4)

my_string = ""
print(len(my_string)) # The empty set. 0 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))
print(alphabet[25])
print(alphabet[1]) #Gives B
print(alphabet[1:5]) #1-5 exlusive.  This is string slicing. 

# LIST START

fruits = ["apple", "banana", "cherry", 1, 100, 3.14, True] 
print(type(fruits))
print(len(fruits)) # prints how many strings: 3

# List can contain objects of different types. 

numbers = [1, 2, 3, 4, 5]
print(len(numbers))

fruits1 = ["apple", "bananas", "cherry", "mango"]
print(fruits1[3]) #prints mango. indexing of list. 
# alphabet[1] = 'b' # strings do not support item assignment. 
fruits1[1]= "Orange"
fruits1.append("Kiwi") #adds Kiwi at the end of the list. 
fruits1.append("Melon") # melon after kiwi
print(fruits1)

coordinates = 4, 5 #tuple because of the comma. 
print(coordinates)

players = {"Messi": 10, "Ronaldo": 7}
print(len(players)) 