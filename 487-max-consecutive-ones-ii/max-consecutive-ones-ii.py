class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


        l = 0
        zero = 0
        """

        Create a sliding window
        Try to get max
        If we exceed constraint, try drecreasing window


        """
        for r in range(len(nums)):
            zero += int(nums[r] == 0)
            if zero > 1:
                zero -= int(nums[l] == 0)
                l += 1
        return len(nums) - l


        