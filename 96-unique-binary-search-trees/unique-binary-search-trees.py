# T(n) = from 

class Solution:

    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += (dp[j] * dp[i - j - 1])

        return dp[-1]



"""
This seems somewhat recursive
That is, we have n numbers teo select from (this seems maybe dp'able)


3

1 -> 1 * 2
2 -> 1 * 1
3 -> 2 * 1 

2 + 2 + 1 = 5






Select i
Then 1 - i

3 5

5 - 3 = 2


3 - 1 = 2 

"""

