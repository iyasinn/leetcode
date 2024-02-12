class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        best = nums[0]
        for n in nums: 
            count += int(n == best) + (-1 * (int(n != best)))
            count, best = (1, n) if count == 0 else (count, best)
        return best