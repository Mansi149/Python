"""
PROBLEM 28
Write a program to print the output of the following poblem statement :-
Write a function translate() that will translate a text into "rövarspråket" 
Swedish for "robber's language". 
That is, double every consonant and place an occurrence of "o" in between. 
Take Input from User?
"""
   
def translate(str):
    consonents='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    print("".join(l+'o'+l if l in consonents else l for l in str))
translate(input("Enter Any String: "))