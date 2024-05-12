class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output = [[-1] * (len(grid[0]) - 2) for _ in range(len(grid) - 2)]

        for row in range(1, len(grid) - 1): 
            for col in range(1, len(grid) - 1):

                largest = 0
                for i in range(row - 1, row + 2): 
                    for j in range(col - 1, col + 2): 
                        largest = max(largest, grid[i][j])

                output[row - 1][col - 1] = largest

        return output 
