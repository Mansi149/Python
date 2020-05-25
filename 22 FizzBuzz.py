"""
PROBLEM 22
Write a Python program which iterates the integers from 1 to 50(included). 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".?
"""
 
for x in range(1, 51):    
    if(x%3 == 0 and x%5 == 0):
        print("FizzBuzz")
    elif(x%3 == 0):
        print("Fizz")
    elif(x%5 == 0):
        print("Buzz")
    else:
        print(x)