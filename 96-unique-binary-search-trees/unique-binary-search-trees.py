class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        
        total = 0

        

        for i in range(1, n + 1):
            left = max(1, self.numTrees(i - 1))
            right = max(1, self.numTrees(n - i))
            total += (left * right)

        return total
        

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

