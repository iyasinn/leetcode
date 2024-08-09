
def testSubGrid(grid, row, col): 
    if len(grid) < row + 3 or len(grid[0]) < col + 3: 
        return False

    numbers = [grid[row + i][col + j] for j in range(0, 3) for i in range(0, 3)]

    # Test uniqueness
    if len(set(numbers)) != len(numbers): 
        return False
    
    # 1 - 9
    for x in numbers: 
        if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9]: 
            return False

    matrix = [[grid[row + i][col + j] for j in range(0, 3)] for i in range(0, 3)]
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(column) for column in zip(*matrix)]
    main_diagonal_sum = matrix[0][0] + matrix[1][1] + matrix[2][2]
    anti_diagonal_sum = matrix[0][2] + matrix[1][1] + matrix[2][0]

    if main_diagonal_sum != anti_diagonal_sum: 
        return False 
    
    for i in range(len(row_sums)): 
        if row_sums[i] != main_diagonal_sum or col_sums[i] != main_diagonal_sum: 
            return False

    return True

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        result = 0

        for row in range(len(grid) - 2): 
            for col in range(len(grid) - 2): 
                result += int(testSubGrid(grid, row, col))

        return result
        