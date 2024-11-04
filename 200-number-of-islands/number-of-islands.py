class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        count = 0

        def sink(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and not visited[r][c]):
                return
            if grid[r][c] == "0":
                return
            visited[r][c] = True
            sink(r - 1, c)
            sink(r + 1, c)
            sink(r, c - 1)
            sink(r, c + 1)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c] and grid[r][c] == "1":
                    count += 1
                    sink(r, c)

        return count

        