import math, random

radius = int(input('Please input the radius:'))
r = random.randint(1,10)

print(f'The radius of the sphere is: {radius}')
volume = (4/3)*math.pi*math.pow(radius,3)
print(f'The volume of a sphere with radius {radius} is {volume:.2f}')

factorial = math.factorial(r)

print(f'The factorial of {r} is {factorial}')