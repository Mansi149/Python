"""
PROBLEM 13
Write a program to print the output of the following poblem statement :-
Compute the position of the object after falling for 10 seconds. 
Output the value meters and assume that the acceleration is -9.81?
"""

time, a = float(input("Enter duration of fall (in sec) : ")), -9.81 
print("Distance travelled by the object :", a * time**2 / 2)
