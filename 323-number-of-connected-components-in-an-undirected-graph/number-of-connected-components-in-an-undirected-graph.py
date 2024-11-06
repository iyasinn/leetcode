class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        unvisited = set(range(n))
        adj = [[] for _ in range(n)]
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        def dfs(n):
            nonlocal unvisited
            if n not in unvisited: 
                return

            unvisited.remove(n)
            
            for other in adj[n]:
                dfs(other)
        
        count = 0
        for i in range(n):
            if i in unvisited:
                dfs(i)
                count += 1
        
        return count
