class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # output = [[-1] * (len(grid[0]) - 2) for _ in range(len(grid) - 2)]
        output = []

        for row in range(1, len(grid) - 1): 
            output.append([])
            for col in range(1, len(grid) - 1):
                largest = max(grid[row-1][col-1:col+2]+grid[row][col-1:col+2]+grid[row+1][col-1:col+2])
                output[-1].append(largest)

        print(output)
        return output 
