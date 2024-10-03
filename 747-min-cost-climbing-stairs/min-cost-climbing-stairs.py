class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1: 
            return 0

        tab = [0] * (len(cost) + 1)

        tab[0] = 0
        tab[1] = 0

        for i in range(2, len(tab)): 
            a = tab[i - 1] + cost[i - 1]
            b = tab[i - 2] + cost[i - 2]
            tab[i] = min(a, b)

        return tab[-1]