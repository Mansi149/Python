"""
PROBLEM 46
Write a program to print the output of the following poblem statement :-
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
for i in range(len(names)):
    names[i] = random.choice(code_names)
print (names)
As you can see, this algorithm can potentially assign the same secret code name 
to multiple secret agents. 
Rewrite the above code using map and lambda?
"""

import random as rd
names = ['Mary', 'Isla', 'Sam']
names = map(lambda x : rd.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']), names)
print ("Desired output :", list(names))