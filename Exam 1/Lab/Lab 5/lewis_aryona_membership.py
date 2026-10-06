'''Aryona Lewis, membership, assigning list to if else statements'''
from string import punctuation
vowels = ['a', 'e', 'i', 'o', 'u']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = [',', ';', '.', '?', '!']

character = input("Please enter a character: ")

if character in vowels:
    print(f"The character '{character}' is a vowel.")
elif character in digits:
    print(f"The character '{character}' is a digit.")
elif character in punctuation:
    print(f"The chracter '{character}' is in punctuation.")
else: 
    print(f"The character '{character}' is a consonent. ")