"""
PROBLEM 49
Write a program to print the output of the following poblem statement :-
Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:  
    Order Number    Book Title              Author      Quantity    Price per Item
    34587           Learning Python         Mark Lutz   4           40.95
    98762           Programming Python      Mark Lutz   5           56.80
    77226           Head First Python       Paul Barry  3           32.95
    88112           Einführung in Python3   Bernd Klein 3           24.99    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 98.85), ('88112', 74.97)]
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.
    Output:
    [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
# Step 1  Solve the problem using for loop
# Step 2  Refactor your Code  - remove the loop and use map and lambda
# Step 3  Refactor your Code  - use the concept of chaining  PYTHONIC CODE
Hint: 
    Write a Python program using lambda and map.
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python, Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
    ] ?
"""

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
         ["77226", "Head First Python, Paul Barry", 3,32.95],
         ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

listx = list( map( lambda x : ( x[0], round( x[2] * x[3] ) ), orders) ) 
print("Desired output 1 :", listx )

listy = list( map( lambda x : x if x[1] > 100 else ( x[0], x[1] + 10 ), map( lambda x : ( x[0], round( x[2] * x[3] ) ), orders ) ) )
print("Desired output 2 :", listy )