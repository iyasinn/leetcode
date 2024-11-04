def bfs(row, col, oranges, visited, currentTime): 
    if not (0 <= row < len(oranges) and 0 <= col < len(oranges[0])):
        return 
    if (oranges[row][col] != 1): 
        return 

    if (currentTime >= visited[row][col] and visited[row][col] != -1):
        return 

    visited[row][col] = currentTime

    bfs(row + 1, col, oranges, visited, currentTime + 1)
    bfs(row - 1, col, oranges, visited, currentTime + 1)
    bfs(row, col + 1, oranges, visited, currentTime + 1)
    bfs(row, col - 1, oranges, visited, currentTime + 1)

# CHECK OUT MULIT SOURCE BFS
class Solution:
    def orangesRotting(self, oranges: List[List[int]]) -> int:

        # O(n^2)    
        visited = [[-1] * len(oranges[0]) for _ in range(len(oranges))] 

        # O(n^2)
        for row in range(len(oranges)): 
            for col in range(len(oranges[0])): 
                if (oranges[row][col] == 2):
                    bfs(row + 1, col, oranges, visited, 1)
                    bfs(row - 1, col, oranges, visited, 1)
                    bfs(row, col + 1, oranges, visited, 1)
                    bfs(row, col - 1, oranges, visited, 1)
        
        time = 0

        # O(n^2)
        for row in range(len(oranges)):
            for col in range(len(oranges[0])):
                if (oranges[row][col] == 1 and visited[row][col] == -1):
                    return -1
                if (oranges[row][col] == 1): 
                    time = max(time, visited[row][col])
        
        return time
        