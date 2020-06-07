"""
PROBLEM 47
Write a program to print the output of the following poblem statement :-
names = ['Mary', 'Isla', 'Sam']
for i in range(len(names)):
    names[i] = hash(names[i])
print (names)
(Hopefully, the secret agents will have good memories and won’t forget each 
other’s secret code names during the secret mission.)
Rewrite the above code using map?
"""

names = ['Mary', 'Isla', 'Sam']
names = map(hash, names)
print("Desired output :", list(names))