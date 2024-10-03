class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: 
            return nums[0]

        tab = [0] * len(nums) 
        tab[0] = nums[0]
        tab[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)): 
            tab[i] = max(nums[i] + tab[i - 2], tab[i - 1])
        

        return tab[-1]
