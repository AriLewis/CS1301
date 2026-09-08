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