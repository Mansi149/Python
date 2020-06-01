"""
PROBLEM 37
Write a program to print the output of the following poblem statement :-
Consider the following problem, where you want to create a new dictionary 
where the key is a number divisible by 2 in a range of 0-10 and 
it's value is the square of the number. 
First write the solution using for loop and then rewrite using Comprehension?
"""

# using loop
dictx = {}
for n in range(0,10,2):
    dictx[n] = n**2
print(dictx)

# using comprehension
dict_new =  { n : n**2 for n in range(10) 
             if n%2 == 0 }
print(dict_new)
