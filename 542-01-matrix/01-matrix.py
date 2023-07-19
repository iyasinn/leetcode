class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        dist = [[-1] * m for _ in range(n)] 
        # Create a 2D array to hold the distances from each cell to the nearest 0

        q = deque()
        # Use a queue to perform breadth-first search (BFS)

        # First pass: add all 0s to the queue and set their distance as 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        # We append all 0s to the queue, as they serve as starting points for the BFS. 
        # We also set their corresponding distances in the 'dist' array to 0 (since they are already 0s)

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        # Define the four possible directions to move in the matrix (right, left, down, up)

        # Second pass: BFS starting from all 0s
        while q:
            x, y = q.popleft()
            # Pop an element from the queue

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # Calculate the next position based on the current position and the direction

                # If the new position is out of bounds or already visited, skip it
                if nx < 0 or nx >= n or ny < 0 or ny >= m or dist[nx][ny] != -1:
                    continue

                # If it's a valid position, set its distance as the current distance + 1 and append it to the queue
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

        # Return the distance matrix
        return dist