
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = [[] for _ in range(n)]
        for start, end in edges:
            adj[start].append(end)

        visited = {}

        if adj[destination]:
            return False

        def dfs(n):
            nonlocal visited
            if len(adj[n]) == 0:
                return n == destination
            elif n in visited:
                return visited[n] == 2
            
            
            visited[n] = 1

            for other in adj[n]:
                if dfs(other) == False:
                    return False
            
            visited[n] = 2
            return True
        
        return dfs(source)

        