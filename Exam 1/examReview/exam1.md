# Exam 1 Review
Topics Covered:
    - Introduction to Py3
    - Variables and Expressions
    - Types
    - Branching
    - Loops (basics)

# Chapter 1 and 2

Two Types of Errors: 
    1. Syntax Error - wrong syntax OR *run-time error* meaning, due to program not being able to understand the code and can not run until the issue is fixed. 
    2. Logical Errors (Run-time erorors) - Error occurs after the program has complied and ran. i.e division of zero. 

Note: *Review Key-words that can't be used in variables* 
-- Review portions of an actual computer and note what they do. 

## Lecture 4
*Garbage Collection* - Once an object is printed, it is no longer needed and is thrown away. 
    - Deleting unused objects is an automatic process called *garbage collection* that frees memory space. **Likely on exam** 

Variables are references of objets stored in memory to be used later. **Do not get garbage collected** 

### Multability vs Immutable
- *Mutibility* indicaates whether the object's value is allowed to be changed. i.e. List 
- *Immutable* can not be changed. i.e. strings and integers, tuples

### Floating Points
- *overflow* occures when a value is too large to be stored in the memory allocated by the intepreter. 
    - maximum is prox. $1.8 x 10^(308)$

### Division and Modulus
- Modulus gives the remainder of division and always gives the right most digit. Always positive **Note: This needs to be reviewed and better understood**

### Math Module. 

'import math'
floor, ceil, factorial, pow. 

'import random'
- randrange() generates random integers within a specific range. **Exlusive**
- randint() inclusive of the last number. 

### From py file

                x = 7
                print(id(x))

- An ID is the exact location of the variable in the memory


                x = 7
                del x 

- x would be garbage collected. 

Note: Division is always a float number. 

Mod 2
    - Odd numbers always 1.
    - Even numbers always 0

## Lecture 5 

### Escape Sequences

- A *new line* character indicates the end of the line of text
- *BackSlash* \ the interpreter recognizes tht item as the start of the special character's two- Item sequence and then looks at the item to determine. 

Examples:

                print("\\home\\users\\)
                print("Name: John O\ 'Donald')
                print("He said, \ "Hello friend!\"")
                print("My name... \nIs John...")
                \t

**Note: What do each of these mean?**

- Escape Sequences can be ignored by using *raw strings* by adding an r before the string. 
- ord() return the encoded integer value of a string.

**Print(Len(Message)) is in the exam**

### Tuple
- Store a collection of data, like a list, but immutable.
- Supports len(), indexing, and other sequence functions.
- uses (5, 10, 20) as an example. 