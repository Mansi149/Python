"""
PROBLEM 32
Write a program to print the output of the following poblem statement :-
Ask the user to enter some text. 
Display the distribution of letters from within the text?
"""
   

import string

counts = {}
for char in input("Enter a string : ").lower():
        if char not in string.ascii_lowercase:
            continue
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

total = sum(list(counts.values()))
for letter, count in counts.items():
    print(f"{ letter } : { count } { int( count / total * 100 )}%")


        