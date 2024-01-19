class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        if len(matrix) == 1: 
            return min(matrix[0])
            
        dp = [copy.deepcopy(matrix[-2]), copy.deepcopy(matrix[-1])]

        for row in range(len(matrix) - 2, -1, -1): 
            dp[0][0] = matrix[row][0] + min(dp[1][0], dp[1][1])
            dp[0][-1] = matrix[row][-1] + min(dp[1][-1], dp[1][-2])

            for col in range(1, len(matrix[row]) - 1):
                dp[0][col] = matrix[row][col]
                dp[0][col] += min([dp[1][col], dp[1][col - 1], dp[1][col + 1]])

            dp[0], dp[1] = dp[1], dp[0]

        return min(dp[1])