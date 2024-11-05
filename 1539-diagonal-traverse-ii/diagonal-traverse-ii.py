
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
                while total >= len(output):
                    output.append([])
                output[total].append(nums[r][c])
        
        sol = []
        print(output)
        for row in output:
            sol = sol + row.copy()[::-1]
        return sol


        