class Solution:

    # rec(n) = rec(n - 1) + rec(n - 2)
    # rec(1) = 2
    # rec(2) = 2

    def climbStairs(self, n: int) -> int:

        if (n <= 2): 
            return n

        first = 1
        end = 1

        for x in range(2, n + 1):
            temp = end
            end += first 
            first = temp
        
        return end

