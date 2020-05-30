"""
PROBLEM 35
Write a program to print the output of the following poblem statement :-
With a given list [12,24,35,24,88,120,155,88,120,155]
Print this list after removing all duplicate values with original 
order reserved ?
"""

listx = [12,24,35,24,88,120,155,88,120,155]
list_out = list(set(listx))
list_out.reverse()
print(list_out)

        