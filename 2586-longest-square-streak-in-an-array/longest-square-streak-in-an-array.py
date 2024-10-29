class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:


        elts = set(nums)
        best = 0

        for n in nums: 

            curr = 1
            val = n 

            while val * val in elts and val < 1000001:
                curr += 1
                val = val * val
            best = max(curr, best)

        return best if best > 1 else -1
        