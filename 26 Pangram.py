"""
PROBLEM 26
Write a Python function to check whether a string is PANGRAM or not
Take input from User and give the output as PANGRAM or NOT PANGRAM?
"""

def pangram_or_not(arg):
  if len('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') == 0 :
    return True
  return False
x = input("Enter a string to check for pangram : ")
if(pangram_or_not(x)):
  print("PANGRAM")
else:
  print("NOT PANGRAM")