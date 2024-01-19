class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = [copy.deepcopy(row) for row in matrix]

        for row in range(len(matrix) - 2, -1, -1): 
            dp[row][0] = matrix[row][0] + dp[row + 1][0]
            dp[row][-1] = matrix[row][-1] + dp[row + 1][-1]

            if len(matrix) > 1: 
                dp[row][0] = min(dp[row][0], matrix[row][0] + dp[row + 1][1])
                dp[row][-1] = min(dp[row][-1], matrix[row][-1] + dp[row + 1][-2])

            for col in range(1, len(matrix[row]) - 1):
                dp[row][col] += min([dp[row + 1][col - 1], dp[row + 1][col + 1], dp[row + 1][col]])

        return min(dp[0])