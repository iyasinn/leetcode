class Solution:
    def jump(self, nums: List[int]) -> int:


        curr = 0
        farthest = 0
        jumps = 0

        for potential in range(len(nums) - 1):

            farthest = max(farthest, potential + nums[potential])

            if potential == curr:
                curr = farthest
                jumps += 1
        
        return jumps
            

        