'''
Author: Aryona Lewis
Program Description: Inputting the lengths of each triangles sides, then finding the perimeter, area, and what type of triangle it is by utilizing if elif statements and inputs.
'''

from math import sqrt
# Prompt the user to input each side of the triangle
A = int(input("Please enter the length of side A of the triangle (in meters): "))
B = int(input("Please enter the lenght of side B of the triangle (in meters): "))
C = int(input("Please enter the length of side C of the triangle (in meters): "))

perimeter = A + B + C
semi = perimeter / 2

area = sqrt(semi* (semi - A) * (semi- B) * (semi - C))

print(f"The perimeter of the triangle is {perimeter}m")
print(f"The area of the triangle is {area} m^2")

if A^2 + B^2 == (C^2):
    print("It is a right triangle")
elif A^2 +B^2 > C^2:
    print("It is an Acute Triangle")
elif A^2 + B^2 < C^2:
    print("It is an Obtuse Triangle")
