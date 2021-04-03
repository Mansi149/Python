"""
PROBLEM 73
By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, WAP to find the sum of the even-valued terms?
"""

prev, cur = 0, 1
sum = 0
while True:
    prev, cur = cur, prev + cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
        sum += cur
print("Sum of even valued terms:", sum)

