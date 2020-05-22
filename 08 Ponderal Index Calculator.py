"""
PROBLEM 8
Write a program to print the output of the following poblem statement :-
Calculate the Ponderal Index of a Person?
"""
Weight, Height = float(input("Enter your weight (in kgs) : ")), float(input("Enter your height (in m) : "))
BMI = Weight / Height**2
print("Ponderal Index :", BMI / Height, "kg/m^3")
