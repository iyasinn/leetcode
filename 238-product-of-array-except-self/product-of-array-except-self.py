class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)
        running_sol = 1
        for i in range(1, len(nums)): 
            solution[i] = solution[i - 1] * nums[i - 1] 
        running_sum = 1
        for i in range(len(nums) - 1, -1, -1): 
            solution[i] *= running_sum 
            running_sum *= nums[i] 

        
        return solution

        