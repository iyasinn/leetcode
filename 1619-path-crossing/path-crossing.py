"""
We could have a set of all points we've been at. And then deal with that. 
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        positions = set()
        move = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        x = y = 0

        for direction in path: 
            if (x, y) in positions: 
                return True
            positions.add((x, y))
            x += move[direction][0]
            y += move[direction][1]
        
        return (x, y) in positions
