class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        sol = []
        for i, h in enumerate(heights): 
            while sol and h >= heights[sol[-1]]:
                sol.pop()
            sol.append(i)
        return sol
        