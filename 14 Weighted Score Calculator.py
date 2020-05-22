"""
PROBLEM 14
Write a program to print the output of the following poblem statement :-
Lets assume there are 3 assignments and 2 exams, 
Each with max score of 100. 
Respective weights are 10%, 10%, 10%, 35%, 35% . 
Compute the weighted score based on individual assignment scores?
"""

A1, A2, A3, E1, E2 = int(input("Enter score of assinment 1 : ")), int(input("Enter score of assinment 2 : ")), int(input("Enter score of assinment 3 : ")), int(input("Enter score of exam 1 : ")), int(input("Enter score of exam 2 : "))
print("\nWeighted Score : ", (((A1 + A2 + A3) * 0.1) + ((E1 + E2) * 0.35)))