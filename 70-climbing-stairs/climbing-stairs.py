class Solution:

    # rec(n) = rec(n - 1) + rec(n - 2)
    # rec(1) = 2
    # rec(2) = 2

    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for _ in range(1, n): 
          dp = [dp[1], dp[0] + dp[1]]
        
        return dp[1]