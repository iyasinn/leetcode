class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        best = 0

        def sink(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            # visited[r][c] = True

            total = 1
            total += sink(r - 1, c)
            total += sink(r + 1, c)
            total += sink(r, c - 1)
            total += sink(r, c + 1)

            return total


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                best = max(best, sink(r, c))

        return best
