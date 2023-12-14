class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])

        row_ones = [0] * NUM_ROWS
        col_ones = [0] * NUM_COLS

        for i in range(NUM_ROWS): 
            for j in range(NUM_COLS):
                if grid[i][j] == 1: 
                    row_ones[i] += 1
                    col_ones[j] += 1

        diff = [[0] * NUM_COLS for _ in range(NUM_ROWS)]
        
        for i in range(NUM_ROWS): 
            for j in range(NUM_COLS):
                diff[i][j] = (2 * row_ones[i]) + (2 * col_ones[j]) - NUM_ROWS - NUM_COLS 
       
        return diff