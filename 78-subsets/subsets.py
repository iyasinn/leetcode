

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = []
        curr = []

        def dfs(nums, curr, output, index):
            if index == len(nums): 
                output.append(curr.copy())
                return

            dfs(nums, curr, output, index + 1)
            curr.append(nums[index])
            dfs(nums, curr, output, index + 1)
            curr.pop()

        dfs(nums, curr, output, 0)
        return output

