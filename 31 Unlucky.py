"""
PROBLEM 31
Write a program to print the output of the following poblem statement :-
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that 
come immediately after a 13 also do not count
Take input from user
Input : 13, 1, 2, 13, 2, 1, 13 
Output : 3 ?
"""
   
thirteen = False
total = 0

for n in input("Enter Numbers -> ").split(" "):
    if int(n) == 13:
        thirteen = True
    
    elif not thirteen:
        total += int(n)
    
    elif thirteen and int(n) != 13:
        thirteen = False

print ("Total of the numbers ->", total)