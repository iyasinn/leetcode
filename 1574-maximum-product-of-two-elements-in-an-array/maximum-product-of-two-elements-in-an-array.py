class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_seen = float("-inf")
        best = 0
        for num in nums:
            best = max(best, (num - 1) * (max_seen - 1))
            max_seen = max(num, max_seen)
        return best
            

        