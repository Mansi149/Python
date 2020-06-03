"""
PROBLEM 41
Write a program to print the output of the following poblem statement :-
Ask the user for the name of a text file. 
Display the final line of that file.
Think of ways in which you can solve this problem, 
and how it might relate to your daily work with Python?
"""

file = input("Enter file name whose last line you want to read : ")
print("Last line of", file, "is", open( file ).readlines()[-1] )

