'''
Aryona Lewis
Calcuating the cost of gas while driving over different distances. 
'''
mpg = float(input("What is your car's gas mileage in miles per gallon: "))
dpg = float(input("What is the cost of gas in dollars per gallon: "))

twenty = 20/(mpg/dpg)
seventy_five = 75/(mpg/dpg)
fivehundred = 500/(mpg/dpg)

print(f"{twenty:.2f} {seventy_five:.2f} {fivehundred:.2f}")