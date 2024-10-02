class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1

        tab = [1, 2]
        tab[0] = 1 
        tab[1] = 2; 

        for i in range(2, n): 
            x = tab[0] + tab[1]
            tab[0] = tab[1]
            tab[1] = x
        
        return tab[1]

        