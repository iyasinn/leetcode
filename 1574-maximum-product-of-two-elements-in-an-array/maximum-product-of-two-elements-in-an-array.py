class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_seen = nums[0]
        best = 0
        for num in nums[1::]:
            best = max(best, (num - 1) * (max_seen - 1))
            max_seen = max(num, max_seen)
        return best
            

        