class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: 
            return nums[0]

        r1, r2 = 0, 0

        for n in nums: 
            t = max(r1 + n, r2)
            r1 = r2 
            r2 = t
        
        return r2
