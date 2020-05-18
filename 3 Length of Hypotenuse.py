"""
PROBLEM 3
Write a program to calculate the hypotenuse of the right angled triangle?
"""
import math
base, height = float(input("Enter base length : ")), float(input("Enter height length : "))
print("Length of hypotenuse :", math.sqrt(base**2 + height**2))
