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

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dx, c + dy)

        # left and right border
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
            
        # top and bottom border
        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)
        
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited:
                    board[r][c] = 'X'
    




        # top and bottom border



        