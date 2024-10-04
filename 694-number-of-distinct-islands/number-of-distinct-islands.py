
"""
We always hit islands from the top left
We can sink stuff so we dont see it again 
And we can take the island and we can extract what we see and haash what we see
All data can be hashed and compared to in O(1), which is very very important to consider!


Idea of relative vs absolute pass
"""



class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        seen = set()

        def dfs(row, col, dirr): 
            nonlocal grid
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): 
                return ""
            elif grid[row][col] == 0: 
                return ""
                
            sig = dirr
            grid[row][col] = 0

            sig += dfs(row, col + 1, "R")
            sig += dfs(row, col - 1, "L")
            sig += dfs(row - 1, col, "U")
            sig += dfs(row + 1, col, "D")
            sig += "|BACK|"
            return sig

        count = 0 

        for row in range(len(grid)): 
            for col in range(len(grid[0])): 
                sig = dfs(row, col, "|START|")
                if sig != "": 
                    print(sig)
                if sig != "" and sig not in seen: 
                    seen.add(sig)
                    count += 1
    
        return count






        