"""
PROBLEM 9
Write a program to print the output of the following poblem statement :-
Calculate the Maximum Heart Rate and Target Heart Rate Range 
( Lower and Higher value ) of a person of a specific age?
"""
    
Age = int(input("Enter your age : "))
Max = 220 - Age
print("Maximum Heart Rate :", Max )
print("Lower Target Heart Rate :", Max * 0.7 )
print("Higher Target Heart Rate :", Max * 0.85 )