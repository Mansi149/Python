"""
PROBLEM 10
Write a program to print the output of the following poblem statement :-
Assume today's temperature in Jaipur is 29 degree Centigrade. 
Calculate the temperate in Degree Fahrenheit and print it.
Calculate the temperature in Degree Kelvin and print it?
"""
 
Temp = int(input("Enter Temperature (in degree centrigrade): "))
print("Temperature is", Temp * 9/5 + 32 ,"Degree Fahrenheit or", Temp + 273 ,"Degree Kelvin")
