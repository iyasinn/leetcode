

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = []
        curr = []

        def dfs(nums, curr, output, index):
            if index < 0: 
                return

            dfs(nums, curr, output, index - 1)

            # add current value, add to output, then go to n - 1
            curr.append(nums[index])
            output.append(curr[0::])
            dfs(nums, curr, output, index - 1)
            curr.pop()
        
        output.append([])
        dfs(nums, curr, output, len(nums) - 1)
        return output


