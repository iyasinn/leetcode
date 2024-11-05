
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        bfs = deque()
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        fresh = 0

        for r in range(n):
            for c in range(m): 
                if grid[r][c] == 2:
                    visited[r][c] = True
                    bfs.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        best = 0

        while bfs:
            # best += 1
            size = len(bfs)
            for _ in range(size):
                r, c = bfs.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dx, c + dy
                    if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] == 0:
                        continue
                    visited[nr][nc] = True
                    bfs.append((nr, nc))
                    fresh -= 1
            if len(bfs) > 0: 
                best += 1
        
        return best if fresh == 0 else -1
    


# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
        
#         bfs = deque()
#         n = len(grid)
#         m = len(grid[0])

#         visited = [[-1] * m for _ in range(n)]
#         fresh = 0

#         for r in range(n):
#             for c in range(m): 
#                 if grid[r][c] == 2:
#                     visited[r][c] = 0
#                     bfs.append((r, c, 0))
#                 if grid[r][c] == 1:
#                     fresh += 1
#         best = 0
#         while bfs:
#             r, c, time = bfs.popleft()
#             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 nr, nc = r + dx, c + dy
#                 if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] != -1 or grid[nr][nc] == 0:
#                     continue
#                 visited[nr][nc] = time + 1
#                 bfs.append((nr, nc, time + 1))
#                 fresh -= 1
#                 best = max(time + 1, best)
        
#         return best if fresh == 0 else -1
    


            

