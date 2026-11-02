'''
Author: Aryona Lewis
Program Description: Inputting the lengths of each triangle's sides, then finding the perimeter, area, and what type of triangle it is by utilizing if elif statements and inputs.
'''

from math import sqrt

# Prompt the user to input each side of the triangle
side_a = int(input("Please enter the length of side A of the triangle (in meters): "))
side_b = int(input("Please enter the length of side B of the triangle (in meters): "))
side_c = int(input("Please enter the length of side C of the triangle (in meters): "))

# Calculate the perimeter and semi-perimeter of the triangle
perimeter = side_a + side_b + side_c
semi_perimeter = perimeter / 2

# Calculate the area of the triangle
area = sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))

# Display the perimeter and area
print(f"The perimeter of the triangle is {perimeter}m")
print(f"The area of the triangle is {area:.2f} m^2")

# Classify the triangle using the Pythagorean inequality
if side_a**2 + side_b**2 == side_c**2:
    print("It is a right triangle")
elif side_a**2 + side_b**2 > side_c**2:
    print("It is an Acute Triangle")
elif side_a**2 + side_b**2 < side_c**2:
    print("It is an Obtuse Triangle")
