class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        seen = defaultdict(int)
        ans = 0

        for prefix in accumulate([0] + nums):
            ans += seen[prefix - k]
            seen[prefix] += 1


        return ans
        