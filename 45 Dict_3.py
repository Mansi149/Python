"""
PROBLEM 45
Write a program to print the output of the following poblem statement :-
Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
1 Get the corresponding `celsius` values in list
2 Create the `celsius` dictionary
3 convert a dictionary of Fahrenheit temperatures into celsius?
"""

fahrenheit = { 't1' : -30, 't2' : -20, 't3' : -10, 't4' : 0 }
list(fahrenheit.items())
dict_cel = {  key : round( ( float( 5 ) / 9 ) * ( val - 32 ), 2 ) for (key, val) in list(fahrenheit.items())   }
print("Desired output :", dict_cel)