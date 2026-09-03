# Review 
Covering Rules for varibles. 

No classes or objects until week 10 of the course. skip 2.3 

Review introduction and how the computer works aka Interpreter. 

# Section 2.3

Garbage Collection. - Once an object is printed it is no longer neded is thrown away. 

Deleting unused objects is an automatic process called *garbage collection* that frees memory space. *** 

Variables are references of objects stored in the memory to be used later. x does NOT get garbage collected.

*multability* indicates whether the object's value is allowed to be changed. such as list. 

Integers and strongs are *immutable* meaning integers and strings.. section 2.3

# 2.4 Floating-Points

- scienetific notation
- *overflow* /*overflowError* occures when a value is too large to be stored in the memory allocated by the intepreter. 
    Maximum is prox. $1.8 x 10^308$

# 2.5 Arithmetic Operators.
** is an exponent in python 

- An expresion *evaluates* to a value which replaces the expression. Ex: if x is 5, then x+1 evaluates to 6, and y = x+1 assigns y with 6. 
- An expression is evaluates using the order of standared mathematics is also known in programming as *presedence rules*
1. Partheses ()
2. Expondent **
3. unary - used for negation
3. * / % multiplication, division, modulus. 
4. x - 

# 2.7 Divsion nad Modulus

- Refer to python code for how the floor division works. Always rounds down. 
- Modulus gives the remainder of division and always gives the right most digit. Always positive number. 

24 % 4 = 1 
-24 = -7 * 4 + 3 This is how mod of negative numbers work. 

# 2.8 Module basics 
 We will cover this more in week 12. 

 - python program code in a file is called a *script* and execute the code by passing the script as input to the python interpreter. 

 # 2.9 Math Module.  
 All the things you can use by using the 'import math' 
 covered: floor, ceil, factorial, pow

 'import random' 
 - useful random functions: 
    - randrange() generates random integers within a specific range. 