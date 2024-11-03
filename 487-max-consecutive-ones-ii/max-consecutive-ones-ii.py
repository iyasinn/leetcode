class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


        l = 0
        zero = 0
        best = 0

        for r in range(len(nums)):
            zero += int(nums[r] == 0)
            while l <= r and zero > 1:
                zero -= int(nums[l] == 0)
                l += 1
            best = max(best, r - l + 1)
        return best


        