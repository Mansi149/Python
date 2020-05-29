"""
PROBLEM 33
Write a Python program that accepts a string from User and calculate the number of digits 
and letters ?
"""

digit = 0
letter = 0
for element in input("Input a string : "):
    if element.isdigit():
        digit = digit + 1
    elif element.isalpha():
        letter = letter + 1
    else:
        pass
print("Letters :", letter)
print("Digits :", digit)

        