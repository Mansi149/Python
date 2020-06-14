"""
PROBLEM 59
Write a program to print the output of the following poblem statement :-
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]
Plot a Bar Graph for the data above ?
"""
     
import matplotlib.pyplot as plot
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

plot.bar(x, energy, align = 'center', orientation = 'vertical', alpha = 0.5, color = 'yellow', edgecolor = 'blue', width = 0.5)
plot.title('Energy Consumption Graph')
plot.xlabel('Source of Energy')
plot.ylabel('Energy (kcal)')