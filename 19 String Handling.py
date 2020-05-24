"""
PROBLEM 19
Write a program to print the output of the following poblem statement :-
Take first and last name in single command from the user and print  
them in reverse order with a space between them, 
find the index using find/index function and then print using slicing concept of the index?
"""
   
name = input("Enter full name : ")
print("Reverse Order :", " ".join(name.split(" ")[::-1]))
