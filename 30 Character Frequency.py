"""
PROBLEM 30
Write a program to print the output of the following poblem statement :-
This program accepts a string from User and counts the number of characters 
(character frequency) in the input string. 
Input : www.google.com
Output : {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3} ?
"""
   
def frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(frequency(input("Enter the string : ")))
               
