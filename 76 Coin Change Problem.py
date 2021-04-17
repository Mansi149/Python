"""
PROBLEM 76
Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} 
valued coins, how many ways can we make the change? The order 
of coins doesn’t matter.For example, for N = 4 and S = {1,2,3}, 
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So 
output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are 
five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and 
{5,5}?
"""

def coin(coins, sum):
    size = len(coins)
    arr = [[0] * (sum + 1) for x in range(size + 1)]
    for i in range(size + 1):
        arr[i][0] = 1
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else: 
                arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]
    return arr[size][sum]
coins = [1, 2, 3]  
sum = 7 
print("Possible ways %s can be made is %s" % (sum, coin(coins, sum)))
