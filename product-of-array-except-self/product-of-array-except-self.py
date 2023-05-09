class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Start getting the left prefix product
        ans = [1]

        for i in range(1, len(nums)):
            ans.append(ans[i - 1] * nums[i - 1])
    
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans

