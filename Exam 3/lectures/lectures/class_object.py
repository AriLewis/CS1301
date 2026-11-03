'''
Class and objects
 attributes, methods, constructors
'''
#this function takes self as an argument. #self is a local variable. 
class Robot:
    def __init__(self, givenName, givenColor, givenWeight):
        self.name = givenName
        self.name = givenColor
        self.weight = givenWeight
    def introduce(self):
        print("My name is", self.name) # self refers to the cunrrent object of the class. 
    
# when you use init you can no longer use default class constructor. 
#r1 = Robot()
#r1.namee = "Tim"
#r1.color = "Blue"
#r1.weight = 40

#r1.introduce()

r1 = Robot("Tim", "Blue", 40) 
r1.introduce()


r2 = Robot("Jerry", "red", 20)
r2.introduce()
'''
Custom Constructor vs.  Default constructor
    - no init, default yes. 
    - init must use costume constructor. 

self should be the first argument passed ** 

- Intance method - any function or method defined within a class is referred to as an instance method. 
    - to call does not need self since self is a local scope within that class. 
'''

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        