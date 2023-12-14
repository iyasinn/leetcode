class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        N, M = len(grid), len(grid[0])

        row_ones = [0] * N
        col_ones = [0] * M 

        for i in range(N): 
            for j in range(M):
                if grid[i][j] == 1: 
                    row_ones[i] += 1
                    col_ones[j] += 1

        diff = [[0] * M for _ in range(N)]
        
        for i in range(N): 
            for j in range(M):
                diff[i][j] = (2 * row_ones[i]) + (2 * col_ones[j]) - N - M 
       
        return diff