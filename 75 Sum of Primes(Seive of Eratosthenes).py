"""
PROBLEM 75
Find the sum of all the primes below two million using 
seive of eratosthenes algorithm?
"""

from math import sqrt  
MAX = 2000000
prefix = [0 for i in range(MAX + 1)]  
def buildPrefix():
    prime = [True for i in range(MAX + 1)]  
    for p in range(2,int(sqrt(MAX)) + 1, 1):          
        if (prime[p] == True):
            for i in range(p * 2, MAX + 1, p):
                prime[i] = False
    prefix[0] = 0
    prefix[1] = 0
    for p in range(2, MAX + 1, 1):
        prefix[p] = prefix[p - 1]
        if (prime[p]):
            prefix[p] += p
def sumPrimeRange(L, R):
    buildPrefix()  
    return prefix[R] - prefix[L - 1]
if __name__ == '__main__':
    L = 2
    R = 2000000
    print('The sum of prime numbers:', sumPrimeRange(L, R))
  
