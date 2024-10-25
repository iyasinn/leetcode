"""
When we cna't move forward, then we have an issue
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0 
        for i in range(len(nums)):
            if i > end:
                return False
            end = min(len(nums) - 1, max(end, i + nums[i]))
        return end == len(nums) - 1




        