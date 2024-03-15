class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)
        left_mult, right_mult = 1, 1
        for i in range(len(nums)): 
            solution[i] *= left_mult
            solution[len(nums) - i - 1] *= right_mult
            left_mult *= nums[i]
            right_mult *= nums[len(nums) - i - 1]

        return solution

        