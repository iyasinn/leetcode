
"""
For diagonals
row index and col index will line up

"""

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        output = []

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                total = r + c
                output.append((total, c, r))
        output.sort()
        return [nums[r][c] for _, c, r in output]


        