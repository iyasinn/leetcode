"""
We can keep a farthest value
And only jump when we reach our current position
Since it is guaranteed we can reach the end, then it is fine
"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        l = 0 
        r = 0

        while r < len(nums) - 1:
            farthest = 0

            while l <= r:
                farthest = max(l + nums[l], farthest)
                l += 1
            
            l = r + 1
            r = farthest
            jumps += 1

        return jumps


        curr = 0
        farthest = 0
        jumps = 0

        for potential in range(len(nums) - 1):

            farthest = max(farthest, potential + nums[potential])

            if potential == curr:
                curr = farthest
                jumps += 1
            
        
        return jumps
            

        