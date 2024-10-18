"""

This feels like brute force simply
Go thru all subsets, get bitwise or

"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        best = 0
        freq = 0

        def dfs(i, curr):
            nonlocal best
            nonlocal freq

            if i == len(nums):
                if curr > best: 
                    freq = 1
                    best = curr
                elif curr == best: 
                    freq += 1
                return

            # dont chooose i
            dfs(i + 1, curr)
            # choose i
            dfs(i + 1, curr | nums[i])
        
        dfs(0, 0)
        return freq
            

        