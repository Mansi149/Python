"""
PROBLEM 7
Write a program to print the output of the following poblem statement :-
Assuming your weight in kilogram and height in meters  
Calculate your BMI value?
"""
Weight, Height = float(input("Enter your weight (in kgs) : ")), float(input("Enter your height (in m) : "))
print("BMI :", Weight / Height**2, "kg/m^2")
