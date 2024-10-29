class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:


        elts = set(nums)
        best = 0

        # O(n)
        for n in nums: 

            curr = 1
            val = n

            if int(sqrt(val)) in elts and float(int(sqrt(val))) == sqrt(val):
                continue

            while val * val in elts:
                curr += 1
                val = val * val

            best = max(curr, best)

        return best if best > 1 else -1
        