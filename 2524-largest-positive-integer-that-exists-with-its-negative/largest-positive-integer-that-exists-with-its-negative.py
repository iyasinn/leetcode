class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        cache = set()

        solution = -1

        for n in nums: 
            if (n * -1) in cache:
                solution = max(solution, abs(n))
            cache.add(n)
        
        return solution
        