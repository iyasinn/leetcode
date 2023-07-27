class Solution:

    # rec(n) = rec(n - 1) + rec(n - 2)
    # rec(1) = 2
    # rec(2) = 2

    def climbStairs(self, n: int) -> int:

        if (n == 1): 
            return 1
        elif (n == 2): 
            return 2
        
        first = 1
        end = 2

        for x in range(3, n + 1):
            temp = end
            end += first 
            first = temp
        
        return end

