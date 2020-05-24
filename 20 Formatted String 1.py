"""
PROBLEM 20
Write a program to print the output of the following poblem statement :-
Input : Welcome to Pink City Jaipur
Output : Welcome*to*Pink*City*Jaipur?
"""
   
strx = input("Enter string : ")
print("Desired string :", "*".join(strx.split()))


