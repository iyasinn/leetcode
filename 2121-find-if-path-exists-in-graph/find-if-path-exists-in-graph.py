class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set([source])
        dfs = deque([source])

        while dfs: 
            top = dfs.popleft()
            if top == destination:
                return True
            
            for other in adj[top]:
                if other in visited:
                    continue
                visited.add(other)
                dfs.append(other)

        return False
