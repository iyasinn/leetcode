class Solution:

    # rec(n) = rec(n - 1) + rec(n - 2)
    # rec(1) = 2
    # rec(2) = 2

    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        
        first = 1
        second = 2

        for _ in range(2, n): 
            first, second = second, first
            second += first
        
        return second

