'''
Author: Aryona Lewis
Program Description: A terminal calculator that reads a full arithmetic
expression, splits it into a left value, operator, and right value,
computes the result, and repeats until the user types a stop word.
'''
# Defining the different types of operations
def addition(left, right):
    return left + right

def subtraction(left, right):
    return left - right

def multiplication(left, right):
    return left * right

def division(left, right):
    return left / right

def modulus(left, right):
    return left % right

def floor_division(left, right):
    return left // right

def power(left, right):
    return left ** right

# def float check
print("----- Terminal Calculator -----")
expression = input("Enter an expression (or 'quit'/ 'q' to stop): ")
