"""
We could have a set of all points we've been at. And then deal with that. 
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        positions = set([(0, 0)])
        move = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        x = 0
        y = 0

        for direction in path: 
            dx, dy = move[direction]
            x += dx
            y += dy
            print(x, y, positions)
            if (x, y) in positions: 
                return True
            positions.add((x, y))

        return False
