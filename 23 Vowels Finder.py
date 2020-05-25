"""
PROBLEM 23
Write a program to print the output of the following poblem statement :-
Remove all the vowels from the list of states
Input : state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Output : ['lbm', 'clfrn', 'klhm', 'flrd'] ?
"""
   
state_name = [ input("Enter state names : ") ]
listx = []
for state in state_name:
    strx = ""
    for letter in state:
        if letter not in "AEIOUaeiou":
            strx = strx + letter
    print(strx)