class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        vis = set()

        adj = [[] for _ in range(n)]
        for start, end in edges: 
            adj[start].append(end)
            adj[end].append(start)
        
        def dfs(node, parent):
            if node in vis:
                return False

            vis.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        val = dfs(0, None)
        return val and len(vis) == n
            
            
        


