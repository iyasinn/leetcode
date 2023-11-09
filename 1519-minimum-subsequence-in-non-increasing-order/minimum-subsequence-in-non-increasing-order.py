class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        first = sum(nums)
        second = 0

        output = []

        for i in range(len(nums)):
            second += nums[i]
            first -= nums[i]
            output.append(nums[i])
            if (second > first):
                break
        
        return output
        