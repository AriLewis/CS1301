# Review 
- Covering import random
    - random()
    - randrange()
    - randint ()

# 2.11 Representing text
- *Unicode* to represent every pissuble character as a unique number known as a *code point*
    - can find the table in this section. 
## Escape sequences 
 - A *newline* character indicates the end of the line of text, encoded as 10. 
- The *backslash* \ the interpreter recognizes that item as the start of a special character's two-item sequence and then looks at the next item to determine. The two item sequence is called an *escape sequence*

print("\\home\\users\\") 
print('Name: John O\ 'Doanld')
print("He said, \"hello friend!\"")
print(My name... \nIs john...")
\t is tab. 

Escape sequences can be ignored using *raw strings*. By adding an r before a string. 

- The built-in function *ord()* returns an encoded integer value of a string of length. 

- note, follow up this section later chr()

*PRINT(LEN(MESSAGE)) IS IN THE EXAM. MESSAGE.LEN() DOES NOT WORK.* 

- strings are inmuttable/ unchangeable. 
- list are mutable.

# 3.3 Tuples 

- A *tuple* stores a collection of data, list a list, but it is immutable. - Once created, the tuple's elements cannot be changed. 
    - supports len(), indexing, and other sequence functions. 
    - (5, 15, 20) is how. 
    - when they are usually used? Coordinates, latitude and longitude.

Skipping sets until Thursday 

# 3.5 Dictionary
- a *dictionary* is a Python container used to describe associative relationships. A dictionary is represented by *dict* object type. 
- Associates (or maps) keys with values. A *key* is a term that can be located in a dictionary, such as cat.
- A *value* describes some data associated with a key. A key can be any immutable type, such as a number, string, or tuple; a value can be any type. 
- A dict object is created using *curly brackets* {} to surround *key:value pairs* that comprise the dictionary contents. 
    - KV Cache ???? 
    