'''
This is all extremely important

Classes +
An object is a grouping of data (variables) and operations can be preformed on that data 
'''

class Robot:
    def __init__(self, name, color, weight): #positional arguments
        self.color = color
        self.weight = weight  #Custom constructor of the class. Used to itialized that object
        self.name = name
    def introduce(self):
        print("My name is", self.name) #Constructor initialize different attributes for that class

my_dict = {}
my_dict1 = dict()

my_list = []
my_list = list() #Constructor examples

my_set = set() #only one way of doing empty set and tuples
my_set = tuple()

#r1 = Robot()
#print(type(r1)) 

'''
After givenName, etc is added into the class, this gives postional arguement error
r1.name = "Tom"
r1.color = "Blue"
r1.weight = 40
r1.introduce() # my name is tom


r2 = Robot()
                Creates typeError
r2.name = "Jerry"
r2.color = "Red"
r2.weight = 30

r2.introduce() # my name is jerry 
'''

r1 = Robot("Tom", "Blue", 40)
r2 = Robot("jerry", "red", 30)

class Person:
    def __init__(self, name, personality, isSitting): #THIS WILL BE IN EXAMPLE KNOWING HOW TO FINISH THE CONSTRUCTOR
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
    
    def sit_down(self):
        self.isSitting = True
    
    def stand_up(self):
        self.isSitting = False

p1 = Person("Alice", "Happy", False)
p2 = Person("Ari", "Sad", True)

print("Before calling sit_down", p1.isSitting)
p1.sit_down()
print("After calling sit_down()", p1.isSitting) #Inside class use self. Outside we use p1.sit_down() for example


print("Before calling stand_up()", p2.isSitting)
p2.sit_down()
print("After calling sit_down()", p2.isSitting) #Inside class use self. Outside we use p1.sit_down() for example

'''
Connecting the two classes. '
'''
p1.robot_owned = r2
p2.robot_ownded = r1

p1.robot_owned.introduce()
#p2.robot_owned.introduce()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

d1 = Dog("Bark", "German Shepard")
d2 = Dog("Arg", "Golden")

print(d1.name) #dot notation is what this is called
print(d2.breed)

'''
Instance attributes VS Class Attributes
    Class attribute is shared
'''
class Car:
    wheels = 4 # class attribute, shared by all instances of the class
    def __init__(self, brand, model):
        self.brand = brand #instance attribute
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels) # prints 4 
print(car1.brand)

# is it possible to modify class attributes? Yes

'''
Modifying instance and class attributes
'''
car1.wheels = 6 #Creates a new instance attribute, does not affect the class.
Car.wheels = 8 # Changes the class atribute for all instances except for car1

print(car1.wheels)
print(car2.wheels)