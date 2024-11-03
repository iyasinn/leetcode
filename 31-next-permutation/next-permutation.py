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

        if l < 0:
            nums.reverse()
            return

        r = l + 1

        for i in range(l + 1, len(nums)):
            if nums[i] > nums[l] and nums[i] <= nums[r]:
                r = i
        
        nums[l], nums[r] = nums[r], nums[l]
        nums[l + 1:] = list((nums[l+1:]))[::-1]
        
        
        

