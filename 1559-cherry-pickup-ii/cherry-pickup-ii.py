"""

For the last row, for any two spots, we can consider each robot in those two spots

Solution at this configuration is:
Now there are 9 cases you can hit
rec(row, r1, r2) = max(test each robot coming from each direction)

dp where 
where you have rows

"""

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        @cache
        def rec(row, r1, r2): 
            if r1 < 0 or r2 < 0 or r1 >= COLS or r2 >= COLS or row >= ROWS:
                return 0

            changes = [0, 1, -1]
            total = 0

            for i, j in list(product(changes, repeat=2)): 
                total = max(total, rec(row + 1, r1 + i, r2 + j))

            if r1 == r2: 
                return grid[row][r1] + total
            return total + grid[row][r1] + grid[row][r2]

        return rec(0, 0, COLS - 1)
            
            


        