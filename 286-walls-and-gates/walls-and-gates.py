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
                    rooms[r][c] = 2147483647
                    bfs.append((r, c, 0))
        
        while bfs: 
            r, c, dist = bfs.popleft()

            if not (0 <= r < n and 0 <= c < m):
                continue
            if rooms[r][c] == -1 or rooms[r][c] < 2147483647:
                continue

            rooms[r][c] = dist

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dx, c + dy
                bfs.append((nr, nc, dist + 1))
            

                




        """
        Do not return anything, modify rooms in-place instead.
        """
        