"""
PROBLEM 48
Write a program to print the output of the following poblem statement :-
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1
    if height_count > 0:
        average_height = height_total / height_count
print (average_height)
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True?
"""

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
listx = list( map( lambda listx : listx['height'], filter( lambda listy :'height' in listy, people ) ))
if len( listx ) > 0 :
    average_height = sum( listx ) / len( listx )
print ( average_height )