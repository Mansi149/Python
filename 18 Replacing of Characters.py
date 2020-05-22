"""
PROBLEM 18
Write a program for a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it?
"""

str1 = "RESTART"
str1[0] + str1[1:].replace(str1[0], "$")
