"""
PROBLEM 38
Write a program to print the output of the following poblem statement :-
Let's suppose you need to create a new dictionary from a given dictionary but 
with items that are greater than 2 ?
"""

dictx = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dictx_cond = { key : val for ( key , val ) in dictx.items() if val > 2 }
print("Desired dictionary is :", dictx_cond)