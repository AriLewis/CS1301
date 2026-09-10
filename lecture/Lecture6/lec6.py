''' This is review from the previous class'''
print("Hi Class")
alphebets = "abcdefghijklmnopqrstuzwxyz"
print(len(alphebets)) #gives length of string. Indexing starts at zero. Max is Len - 1. 
print(alphebets[0]) #how we get the letter A
print(alphebets[25]) #prints z
print(alphebets[1:5]) #slicing, ending exclusive. bcde

fruits = ["Apple", "Banana", "Cherry"] #list
print(len(fruits))

fruits1 = ["Apple", "Banana", "Cherry", 100, 3.14, True, False] #can have all elements
fruits.append("grapes") #adds grape to the end of fruits

''' Lecture 6 New stuff'''

fruits = ["Apple", "Banana", "Cherry"]
fruits.pop(1) #Removes Banana
print(fruits)
fruits.append("Grape")
print("Original List", fruits)
fruits.pop(2)
print("Updated list", fruits)

fruits.pop() #removes the very last item. 
print(fruits) 



fruits = ["Apple", "Banana", "Cherry", "Grapes"]
fruits.remove("Cherry")
print(fruits) #pop function requires a certain index. Remove function removes specific element such as "Cherry"
fruits.pop(1)
item_removed = fruits.pop(1)
print("Updated List: ",fruits)
print(item_removed) #pop removes and returns. Remove does NOT. 

numbers = [100, 150, 80, 50, 10, 200, 45]
print(max(numbers)) #prints maximum number in the list. 
print(min(numbers)) #prints the minimum number in the list
print(sum(numbers))

my_list = [] #empty list.
print(len(my_list)) 
mixed = fruits + numbers
print(mixed) #appends or adds the number list to the end of fruits. 

coordinates =(10,20) #tuples
colors = ("red", "blue", "green")
print(coordinates) #you can create tuples without parentheses. 
# the COMA makes them the tuple

print(colors[2])
 #colors[2] = pink invalid and gives error

fruits = {"apple", "banana", "cherry", "apple"} #removes the duplicate of apple
print(fruits)
print(len(fruits))

numbers = {2, 4, 6}
numbers.add(8) # For numbers, you use the add function, NOT THE APPEND. 
print(numbers)
print(type(numbers))

set1 = {}
print(type(set1)) #Empty {} creates an empty dictonary. 

set1 = set() #how you create an empty set. 
print(type(set1))

list1 = list() #list constructor.
print(type(list1))

tuple1 = tuple()
print(tuple)

prints = ("apple")
print(type(prints)) #gives string type

numbers = (100)
print(type(numbers)) # integer type

fru = ("apple",)
print(type(fru)) # Comma makes it a tuple at the end THIS WILL BE IN THE TEST

fruits = {"apple", "banana", "cherry"} #back to sets
fruits.remove("banana")
print(fruits)

fruits = {"apple", "banana", "cherry"} #back to sets
#fruits.pop(1) Because sets are unordered, this gives an error. fruits.pop() randomly picks.property
print(fruits)

'''Set Operations'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.union(b) # I know what union means. 
print(c)

d = a.intersection(b)
print(d) #again, I know what intersection means. 

e = a.difference(b) #gives 1,2
print(e)

f= b.difference(a) #gives 5,6 
print(f)

g = a.symmetric_difference(b) # the union of the two sets, minus their intersection. 
print(g) #{1,2,5,6}

''' Dictionary '''

car = {"make": "Toyota",
                        "model": "camary",
                        "Year": 2018}
# The three keys here are make, model, and year. 

print(car) #prints the key and value. 

student = {
    "name": "mario",
    "age": 18,
    "gpa": 3.85    
}
print(student)

print(car["model"]) #gives value of a certain key. 
print(car["Year"])
# Keys are unique, prints the most recent value of the key. 
print(len(car)) 

car["model"] = "Rav4" #how you update the dictionary by accessing the kv. 
print(car)
car["color"] = "Blue" #adds a new entry of the dictionary. 

print(car)

print(f"{3*3}") #prints 9
print(f"{3*3=}") # prints 3*3=9 shows operation and resulting number. 