"""
PROBLEM 60
Write a program to print the output of the following poblem statement :-
For our first pie chart, 
the data we will plot describes the number of students
who choose different engineering majors at 
colleges in the US each year.

Discipline              Number of graduates
Civil Engineering       15,000 graduates
Electrical Engineering  50,000 graduates
Mechanical Engineering  45,000 graduates
Chemical Engineering  10,000 graduates ?
"""
     
import matplotlib.pyplot as plot

Discipline = ['Civil', 'Electrical', 'Mechanical', 'Chemical']
Graduates = [15000, 50000, 45000, 10000]

plot.title('Graduates in different Disciplines')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plot.pie(Graduates, 
        labels = Discipline,
        colors = colors,
        autopct ='%1.2f%%', 
        shadow = True, 
        startangle = 90)
plot.axis('equal')  