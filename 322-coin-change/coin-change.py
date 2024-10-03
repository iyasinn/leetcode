"""
Brute force
Well we have coins of different denominations, and we have the array, and we need to use as few coins
as possible. 

Brute force: Try all possible ways to select coins and then select the one fewest
n coin types -> m

2^m -> exponential

----------

Greedy approach
[1, 2, 3]  ->   1
3, 3
3, 3, 2
3, 1

Use as many big coins as possible
Mathematically proving greedy is difficult 

- Greedy works for all cases
- Greedy does not work for at least one case -> There exists a case where greedy does not exist

[1, 3, 5] -> 9

5, 1 1 1 1 ->  5 coins
3 -> 3 coins
3, 5, 9, 12, 15


Denominations will work 
T(n) = for all coins x that are <= n: T(n - x) eventually gets to zero 
And keep trying this for all numbers as long as x is possible 


"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(n): 
            if n == 0: 
                return 0 
            if n < 0: 
                return -1
            
            minCost = float('inf')
            found = False

            for c in coins: 
                val = dfs(n - c)
                if val != -1: 
                    minCost = min(val + 1, minCost)
                    found = True
            
            return -1 if not found else minCost
        
        return dfs(amount)
            











