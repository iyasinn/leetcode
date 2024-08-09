

def getDir(x): 
    return abs(x) // x

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        # Both the direction and the magnitude 
        dRow = 1
        dCol = 0

        # Count -> steps for magnitude
        countRow = abs(dRow)
        countCol = abs(dCol)

        # That when one is active, the other d is 0 and its count is 0

        total = rows * cols
        visited = []

        while len(visited) < total: 

            if (0 <= rStart < rows and 0 <= cStart < cols): 
                visited.append([rStart, cStart])

            if countRow > 0: 
                cStart += getDir(dRow) 
                countRow -= 1
            elif countCol > 0: 
                rStart += getDir(dCol)
                countCol -= 1

            if dRow != 0 and countRow == 0: 
                dCol = dRow
                countCol = abs(dCol)
                dRow = 0
            elif dCol != 0 and countCol == 0:
                dRow = (abs(dCol) + 1) * (getDir(dCol) * -1) 
                countRow = abs(dRow)
                dCol = 0 
        
        return visited

            


                

        