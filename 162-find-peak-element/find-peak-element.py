
def isPeak(nums, index):
    left = float('-inf') if index - 1 < 0 else nums[index - 1]
    right = float('-inf') if index + 1 >= len(nums) else nums[index + 1]

    return left < nums[index] > right

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0 
        r = len(nums)

        while l < r: 
            m = (l + r) // 2
            print(m)

            if isPeak(nums, m):
                return m
            
            left = float('-inf') if (m - 1) < 0 else nums[m - 1]

            if nums[m] > left:
                l = m + 1
            else: 
                r = m

        return -1
            

                

            

        