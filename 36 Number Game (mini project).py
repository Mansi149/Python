"""
PROBLEM 36 MINI PROJECT
Write a program to print the output of the following poblem statement :-
"""
"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

import random as rd 

if ( int(input(" Pick a number between 1 and 10 : ") ) == rd.randint(1,10) ) :
    print( " Player Wins and Computer Loses " )
    print ( " Player Wins and Computer Loses " )
else :
    print ( " Player Loses and Computer Wins " )
    
"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

import random as rd 
num = rd.randint(1,10)
pred = int(input(" Pick a number between 1 and 10 : ") )
if ( pred == num ) :
    print( " Player Wins and Computer Loses " )
else :
    print ( " Player Loses and Computer Wins " )
    print ( " Player's prediction was {} but Computer chose {}".format (pred, num) )
    
"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""

import random as rd 
num = rd.randint(1,10)
pred = int(input(" Pick a number between 1 and 10 : ") )
if ( pred == num ) :
    print( " Player Wins and Computer Loses " )
else :
    print ( " Player Loses and Computer Wins " )
    print ( " Player's prediction was", pred, "but Computer chose", num ) 
    if (pred < num ) :
        print ( " Player guessed LOW" ) 
    elif (pred > num ) :
        print ( " Player guessed HIGH" ) 

"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""

import random as rd 
num = rd.randint(1,10)

while (1):
    pred = int(input(" Pick a number between 1 and 10 : ") )
    if ( pred == num ) :
        print( " Player Wins and Computer Loses " )
        break
    else :
        print ( " Player Loses and Computer Wins " )
        
"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""

import random as rd 
num = rd.randint(1,10)

guess = 0
chance = 6
while (guess < chance):
    pred = int(input(" Pick a number between 1 and 10 : ") )
    if ( pred == num ) :
        print( " Player Wins and Computer Loses " )
        break
    else :
        guess += 1
        print ( " Player Loses and Computer Wins " )
print ( " Player's prediction was", pred, "but Computer chose", num ) 

"""
Challenge 6
    Print the number of tries left 
"""

import random as rd 
num = rd.randint(1,10)

guess = 0
chance = 6
while (guess < chance):
    pred = int(input(" Pick a number between 1 and 10 : ") )
    if ( pred == num ) :
        print( " Player Wins and Computer Loses " )
        break
    else :
        guess += 1
        print ( " Player Loses and Computer Wins " )
        print ( " You have", chance - guess, "chance left" )
print ( " Player's prediction was", pred, "but Computer chose", num )     

"""
Challenge 7
    Lets give user the option to play again
"""

answer = input("Lets play : ")
if (answer == 'yes'):
    
    import random as rd 
    num = rd.randint(1,10)

    guess = 0
    chance = 6
    while (guess < chance):
        pred = int(input(" Pick a number between 1 and 10 : ") )
        if ( pred == num ) :
            print( " Player Wins and Computer Loses " )
            break
        else :
            guess += 1
            print ( " Player Loses and Computer Wins " )
            print ( " You have", chance - guess, "chance left" )
    print ( " Player's prediction was", pred, "but Computer chose", num )   
else :
    exit()



