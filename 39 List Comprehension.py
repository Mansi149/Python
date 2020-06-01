"""
PROBLEM 39
Write a program to print the output of the following poblem statement :-
For all the numbers 1-1000, use a list comprehension to find numbers is divisible by 3 ?
"""

listx = [ number for number in range( 1 , 1000 ) if number % 3 == 0 ]
print("Desired output : ", listx )