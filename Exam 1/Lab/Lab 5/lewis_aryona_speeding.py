''' Aryona Lewis, Speeding, Giving two integers representing a speed limit in MPH and output'''

speed = int(input("Please enter the speed limit for the road: "))
recorded = int(input("Please enter the vehicle's recorded speed: "))
difference = recorded-speed
if difference <= -10:
    print("The speeding fine is $50")
elif difference > 6 and difference < 21:
    print("The speeding fee is $75")
elif difference > 21 and difference < 41:
    print("the speeding fine is $150")
elif difference > 41:
    print("The speeding fee is $300")
else:
    print("There is no fine.")