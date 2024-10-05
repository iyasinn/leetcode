# So to get to point d[i], the question is, where can we have come from? 
# We can go to all dp[i - j] where we coul dhave jumped to those
# Can we apply our greedy technique here, jump as far right as possible as long as its possible to get there
# Guaranteed we can get to n - 1

class Solution:
    def jump(self, nums: List[int]) -> int:

        curr = 0
        farth = 0
        jumps = 0

        for i in range(len(nums)):

            if curr == len(nums) - 1: 
                break

            farth = min(len(nums), max(i + nums[i], farth))

            if i == curr: 
                curr = farth
                jumps += 1
        
        return jumps
        
