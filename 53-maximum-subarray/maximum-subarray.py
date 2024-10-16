

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        lowest_pre = 0
        curr_pre = 0
        best = float('-inf')

        for n in nums: 
            curr_pre += n
            best = max(best, curr_pre - lowest_pre)
            lowest_pre = min(lowest_pre, curr_pre)
        
        return best


