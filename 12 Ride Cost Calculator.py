"""
PROBLEM 12
Write a program to print the output of the following poblem statement :-
Assume you travel 80 km to and fro in a day. 
Cost of Fuel per litre is 80 INR 
Your vehicle Fuel Average is 18 km/litre. 
Now calculate the cost of driving per day to office.
Take the distance travelled, cost of diesel and Fuel Average from input ?
"""

Dist, Fuel_avg, Fuel_cost = float(input("Enter distance travelled : ")), float(input("Enter vehicle average : ")), float(input("Fuel cost (per litre) : "))
Fuel_cons = float(Dist / Fuel_avg)
print("\nFuel Consumption is", Fuel_cons) 
print("\nCost per day is :", Fuel_cost * Fuel_cons)
