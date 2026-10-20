'''
1. Positional Arguments
2. Keyword Arguments ===============> (by = 1)
3. Arbitrary Arguments =============> (*args)  ----- tuple
4. Arbituary keyword Arguments =====> (**kwargs) ---- dictionary
'''
def print_address(**kwargs):
    for key, value in kwargs.items(): # NOTE THE DIFFERENCE HERE WITH .ITEMS VS .VALUE
        print(f"{key}: {value}") # .ITEMS ONLY WAY TO DO BOTH VALUE AND KEY

print_address(street = "1 Park Place",
                city = "Atlanta",
                state = "GA",
                zip = 30303 )

def shipping_label(*args, **kwargs): #args should always come first. passing both args and kwargs at the same time. 
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

'''
values = "aeiouAEIOU"
text = "Hello World" ----> 3 vowels 
'''

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("Python"))

'''
important algoirthms
'''
def get_evens(numbers): #numbers is [1,2,3,4,5,6,7,8] 
    evens =[]
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

my_list = [1,2,3,4,5,6,7,8]
print(get_evens(my_list))

sentence = "the cat sat on the mat the cat"
words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat"]


# this assigns all the words and how many of each
def word_frequency(sentence):
    freq = {} #empty dic
    words = sentence.split() #splits character by wide space
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

result = word_frequency("the cat sat on the mat the cat")
print(result)

'''
Introduction to Scope
1. Local Scope: A variabled created inside a function belongs to the local scope of that function.
2. global scope: A variable created in the main body Python code is a global variable and belongs to the global scope. 
    - if you need to create,  but are stuck in the local scope, you can use global keyword.
'''

#Local Scope

def myfunc():
    x = 300
    print(x)

myfunc()
# print(x)  error x is not defined. x is a local variable inside the def myfunc()

def myfunc():
    x = 300 #available to any function within the function
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global Scope

x = 300

def myfunc():
    print(x)

myfunc()

def myfunc():
    global x #how you create a global variable. 
    x = 200

myfunc()
print(x)

x = 400
def myfunc():
    x = 100
    print(x)

myfunc()
print(x)

'''
Naming Variable
if you operate with the same variable name inside and outside of the function, Python will treat them as two seperate variables,
one available in the global scope (outside func) and one vailable in the local scope. (inside func)
'''