"""
Feels like a multi source bfs
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        n = len(rooms)
        m = len(rooms[0])

        bfs = deque()
        for r in range(n):
            for c in range(m):
                if rooms[r][c] == 0:
                    bfs.append((r, c, 0))
        
        while bfs: 
            r, c, dist = bfs.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dx, c + dy
                if not (0 <= nr < n and 0 <= nc < m) or rooms[nr][nc] == -1 or rooms[nr][nc] != 2147483647:
                    continue
                bfs.append((nr, nc, dist + 1))
                rooms[nr][nc] = dist + 1
            
        return 

                




        """
        Do not return anything, modify rooms in-place instead.
        """
        