
# Simple BFS
# Directed Graph
# No weight to each node
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [()]
        n = len(grid)
        m = len(grid[0])

        # row, col, length
        bfs = [(0, 0, 1)]

        while bfs:
            row, col, length = bfs.pop(0)

            if row < 0 or row >= n or col < 0 or col >= m:
                continue
            if (row, col) in visited:
                continue
            if grid[row][col] == 1: 
                continue

            visited.add((row, col))

            if row == n - 1 and col == m - 1:
                return length

            for drow in range(-1, 2):
                for dcol in range(-1, 2):
                    if drow == 0 and dcol == 0: 
                        continue
                    nrow, ncol = row + drow, col + dcol
                    bfs.append((row + drow, col + dcol, length + 1))
                    
        return -1


        