class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        l = 0
        curr = 0
        sol = 0
        seen = set()

        for r in range(len(nums)):
            while l <= r and (nums[r] in seen) or (r - l + 1 > k):
                seen.remove(nums[l])
                curr -= nums[l]
                l += 1

            curr += nums[r]
            seen.add(nums[r])

            if r - l + 1 == k:
                sol = max(sol, curr)

        return sol


         