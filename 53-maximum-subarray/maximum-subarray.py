

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sub = nums[0]
        best = nums[0]
        for n in nums[1:]: 
            sub = max(n, sub + n)
            best = max(best, sub)
        return best



        # lowest_pre = 0
        # curr_pre = 0
        # best = float('-inf')

        # for n in nums: 
        #     curr_pre += n
        #     best = max(best, curr_pre - lowest_pre)
        #     lowest_pre = min(lowest_pre, curr_pre)
        
        # return best


