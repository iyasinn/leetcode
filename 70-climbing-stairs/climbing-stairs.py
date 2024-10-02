class Solution:
    def climbStairs(self, n: int) -> int:
        """
        For eacch stair, we can get to it from previous or prev - 2
        What gives away this is dp? 
        T(n) = T(n - 1) + T(n - 2) 
        DP because we have overlapping subacases

        """
        if n == 1: 
            return 1
        tab = [0] * n
        tab[0] = 1 
        tab[1] = 2; 

        for i in range(2, len(tab)): 
            tab[i] = tab[i - 1] + tab[i - 2]
        
        return tab[-1]

        