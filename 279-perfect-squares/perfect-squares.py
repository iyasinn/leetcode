"""
0:00
n^2 is a perfect square
Potentially we can employ a greedy approach, let's just think about it

Given a number n 
There exists some largest perfect square that we can subtract from n

n - L
Then we can now reduce the problem to numSquares(n-L) + 1
The question is, what can we say about L
1 <= L <= n^2
or 
1 <= L <= n 
So we need to consider all x^2 from 1 to N and find the largest possible 

When considering of dp 



The fastest way to get to a number is if it's a perfect square, because if it is, it takes 1 step to get to tha tnumber 
n - perfect
closest = rec(n - perfect_square) + 1
sqrt(n)
"""


class Solution:
    def numSquares(self, n: int) -> int:

        @cache
        def rec(n):
            if n == 0: 
                return 0 
            # if sqrt(n) == int(sqrt(n)): 
            #     return 1
            
            best = n    
            i = 1
            while (i * i <= n):
                best = min(best, rec(n - (i * i)) + 1)
                i += 1
            
            return best 
    
        return rec(n)



