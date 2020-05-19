"""
PROBLEM 5
Write a program to get the total cost of the product with taxes imposed by the government?
"""

Cost, CGST, SGST, Total = float(input("Enter the product cost : ")), float(input("Enter the % CGST : ")), float(input("Enter the % SGST : ")), 0
CGST, SGST = Cost * CGST/100, Cost * SGST/100
Total = Cost + CGST + SGST
print("\nTotal cost of product : ",Total)