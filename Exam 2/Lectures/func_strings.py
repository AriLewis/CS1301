def myfunc():
    x = 300
    print(x)
myfunc()
#print(x) - name error because x is locally defined. 

def greet():
    message = "Hello world!"
    print(message)

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)

'''
Global Keyword
'''
def myfunc():
    global x 
    x = 300

myfunc()
print(x)

x = 300

def myfunc():
    global x #if another global, this CHANGES it. 
    x = 200

myfunc()
print(x)

count = 0
def increment():
    global count
    count += 1
    print("Inside function: ", count)

increment()
print("Outside function: ", count)

#count = 0
#def increment():
    # count = count + 1
   # print(count) unbound local error. must use global
#increment()

'''
New content: strings
'''

letters = "ABCDEfgHIJK"
print(len(letters))
print(letters[0]) #what character is at len 0, it's a
print(letters[10]) #must be lens - 1
print(letters[1:5]) #exlusive  len 5

print(letters[1:10:2])

letters = "ABCDEfgHIJK"
print(letters[-1]) # prints k and so forth for each negative
print(letters[-5:-1]) # ghij k exlusive. 
print(letters[-5:-1:2]) #GI 
print(letters [-1:-10:-1]) #KJIHgfEDC
print(letters[1::5]) #bg
print(letters[:4]) #start from a to 4 exlusive
print(letters[::]) #prints everything
print(letters[::-1]) #prints all backwards
'''
Q: Do we have negtive steps? Yes it just goes backwards.
'''

'''WILL BE ONE OF THE SHORT AWNSER QUESTIONS ON EXAM'''

def is_palindrom(word):
    if word [::] == word[::-1]:
        return True
    else:
        return False

print(is_palindrom("racecar")) #True 
print(is_palindrom("book")) #False

def is_pal(word):#Shortened way of writing the function. THIS EXAMPLE WILL BE IN THE EXAM !!!
    return word [::] == word[::-1]

print(is_pal("racecar"))

'''
Upper(), lower(), title(), capitalize()
'''
name = "hello, world!"
print(name.upper()) # all letters uppercase 
print(name.lower()) # all lower case 

sentence = "the Quick Brown Fox"
word = "pYTHON"
print(sentence.capitalize()) # gives first letter capital and rest lower case. 
print(word.capitalize())

book = "the lord of the rings"
print(book.title()) # First letter of every word is capital

'''
Capitalize vs Title 
cap - only first letter cap and rest lower case 
title - capitalize first letter of every word
'''

'''
Searching Inside String: find() ==> returns the index of the first occurence of a substring

'''

text = "I love Python and Python loves me"
print(text.find("Python")) # returns 7, location
print(text.find("Java")) # prints -1 if not in the string. 

print(text.find("Python", 10)) #search from index 10 to that substring. Prints 18

# replace(old,new)
text = "I like cats. Cats are great."
print(text.replace("cats", "dogs")) # only replaces the first one. 

# Removing whitespaces strip()

user_input = "      hello world.      "
print(user_input.strip()) #Removes whitespaces. 

# Split and join ********** VERY VERY IMPORTANT
'''
split(seperator) breaks a string into a list of substrings at each occurence of the seperator. If no seperator is given, it splits on whitespace,

'''

sentence = " the quick brown fox"
words = sentence.split() #CREATES A LIST OF THE WORDS OF THE SENTENCE. 
print(words) 

words = sentence.split('h')
print(words) # moves the h in the string and outputs a list

cvs_line = "Alice, 30, Engineer"
parts = cvs_line.split(",")

print(parts)

# Join (iterable) is the reverse of split(). 
# It joins elements of a list into a single string using the 
# string it is called on as the seperator

words = ["Python", "is", "fun"]
result = " ".join(words)
print(result) #combines in between words, not a. list