class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        @cache
        def dfs(r, c):
            if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
                return 0
            if matrix[r][c] == 0:
                return 0

            return 1 + min(dfs(r - 1, c - 1), min(dfs(r - 1, c), dfs(r, c - 1)))

        amount = 0
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])):
                amount += dfs(row, col)
        return amount

        