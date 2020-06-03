"""
PROBLEM 40
Write a program to print the output of the following poblem statement :-
create a file absentee.txt
The program should take max 25 students name one by one
When the user enter a blank line, it should terminate the input
Store all the name of students in the file    
Once all the students names have been entered, it should display the list ?
"""
   
with open('absentee.txt','w') as file:
    for student in range(25):
        student = input("Enter absent student name : ")
        if (student == ""):
            break
        file.write(student+'\n')   

file = open('absentee.txt','r')
print (file.readlines())




