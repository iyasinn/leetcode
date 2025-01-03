class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        adj = [[] for _ in range(n)]
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        def dfs(n):
            nonlocal visited
            if n in visited: 
                return

            visited.add(n)

            for other in adj[n]:
                dfs(other)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
