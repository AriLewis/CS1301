'''
Aryona Lewis
Guessing my number out of 10 attempts.
'''
import random

max = 10
number = random.randint(1, 100)

print(f"I have generated a number between 1 and 100. You will have {max} attempts to guess that number.")
for attempt in range(1, max + 1):
    guess = int(input(f"Guess {attempt}: "))

    if guess == number:
        print("You correctly guessed my random number!")
        break
    elif guess > number:
        print("Your guess is greater than my random number. Try Again.")
    else:
        print("Your guess is less than my random number. Try Again.")
else:
    print("You have run out of attempts.")
