"""
PROBLEM 16
Write a program to print the area and perimeter of a circle?
"""

import math
rd = float(input("Enter the radius of the circle : "))
Circumference = 2*math.pi*rd
Area = math.pi*math.pow(rd,2)
print("circumferece is", Circumference)
print("area is", Area)
