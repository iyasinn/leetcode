class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        visited = set()

        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < m):
                return
            if board[r][c] == 'X':
                return
            if (r, c) in visited:
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # left and right border
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)
        
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited:
                    board[r][c] = 'X'
    




        # top and bottom border



        