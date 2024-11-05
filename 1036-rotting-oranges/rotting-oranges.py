class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        bfs = deque()
        n = len(grid)
        m = len(grid[0])

        visited = [[-1] * m for _ in range(n)]

        for r in range(n):
            for c in range(m): 
                if grid[r][c] == 2:
                    visited[r][c] = 0
                    bfs.append((r, c, 0))
        
        while bfs:
            r, c, time = bfs.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dx, c + dy
                if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] != -1 or grid[nr][nc] == 0:
                    continue
                visited[nr][nc] = time + 1
                bfs.append((nr, nc, time + 1))

        print(visited)
        best = 0
        for r in range(n):
            for c in range(m): 
                if grid[r][c] == 1 and visited[r][c] == -1:
                    return -1
                elif grid[r][c] == 1:
                    best = max(visited[r][c], best)
        return best

            

