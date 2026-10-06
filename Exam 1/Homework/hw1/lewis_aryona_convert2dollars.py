'''
Aryona Lewis
Calculating the total amount of money from different cents
'''

nickles = int(input("How many nickles do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))

dollars = nickles * 0.05 + dimes * .10 + quarters * .25

print(f"Amount: ${dollars:.2f}")