"""
PROBLEM 42
Write a program to print the output of the following poblem statement :-
Let’s start with a very simple file of words taken from the text of 
Romeo and Juliet. (romeo.txt)
We will write a Python program to read through the lines of the file
break each line into a list of words
and then loop through each of the words in the line,
and count each word using a dictionary?
"""

dictx = {}
with open("romeo.txt",'r') as file:
    for line in file:
        for word in line.split():
            word.lower()
            if word in dictx:
                dictx[word] = dictx[word]+1
            else:
                dictx[word]=1
print("Desired output : \n", dictx)