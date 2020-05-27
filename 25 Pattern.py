"""
PROBLEM 25
Write a Python program to construct the following pattern :-
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

n = int(input("Enter a numberr : "))
for number in range(n):
    print ("*"*number)
for number in range(n, 0, -1):
    print ("*"*number)