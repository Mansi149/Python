"""
PROBLEM 29
Write a program to print the output of the following poblem statement :-
You are required to write a program to sort the (name, age, height) 
tuples by ascending order where name is string, age and height are numbers. 
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score. 
The priority is that name > age > score 
Aces can be 1 or 11! The number used is whichever gets the highest score.  
Input :
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
Output : [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]?
"""
   
listx = []
while (1):
    x = input("Enter name, age, score : ")
    if not x:
        break
    name, age, score =x.split(',')
    listx.append( (name, int(age), int(score)))
listx.sort()
print(listx)                
