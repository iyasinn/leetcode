"""

So for left pointer
We can keep going up the left side
We keep as long as left <= r

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        l = len(nums) - 2

        while l >= 0 and nums[l] >= nums[l + 1]:
            l -= 1

        if l >= 0:
            r = len(nums) - 1
            while nums[r] <= nums[l]:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        
        nums[l + 1:] = nums[l+1:][::-1]
        
        
        

