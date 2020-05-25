"""
PROBLEM 24
Write a program that asks the user, again and again, to enter a number.
When the user enters an empty string, then stop asking for additional inputs.
Along the way, as the user is entering numbers, 
I want you to store those numbers in a list. 
I also want you to keep track of the minimum and maximum values that you've seen so far.
When the user has finished entering numbers, your program should print out:
The sum of these numbers
The average (mean) of these numbers
The largest and smallest numbers you received from the user ?
"""

numbers = []
largest = None
smallest = None
while True:
    x = input("Enter a number -> ").strip()
    if not x:
        break
    x = int(x)
    numbers.append(x)
    if (smallest is None or x < smallest):
        smallest = x
    if (largest is None or x > largest):
        largest = x
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Sum: {sum(numbers)}")
print(f"Mean: {sum(numbers) / len(numbers)}")
