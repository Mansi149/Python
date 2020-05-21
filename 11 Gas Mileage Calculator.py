"""
PROBLEM 11
Write a program to print the output of the following poblem statement :-
Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
Calculate the average of my car?
"""

Dist, Lit = float(input("Enter the distance travelled : ")), float(input("Enter fuel filled : "))
print("\nGas Mileage is", Dist / Lit, "km/l")