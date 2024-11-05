
"""
I feel we can just a dfs for every single cell
And if a cell hits a cell that goes to pacific and goes to atlantic, then that is a valid cell

How do we store if a cell can go to pacific or atlantic, 

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(visited, r, c):
            if (r, c) in visited: 
                return 

            visited.add((r, c))
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dx, c + dy
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                elif heights[nr][nc] >= heights[r][c]:
                    dfs(visited, nr, nc)
        
        for i in range(m):
            dfs(pacific, 0, i)
            dfs(atlantic, n - 1, i)
        
        for i in range(n):
            dfs(pacific, i, 0)
            dfs(atlantic, i, m - 1)

        return list(pacific.intersection(atlantic))






            
            


    



        # If it can flow to 




        