class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        dfs = deque([source])

        while dfs: 
            top = dfs.popleft()
            if top == destination:
                return True
            if top in visited:
                continue

            visited.add(top)
            
            for other in adj[top]:
                dfs.append(other)

        return False



# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

#         adj = [[] for _ in range(n)]
#         # bidirectional
#         for a, b in edges:
#             adj[a].append(b)
#             adj[b].append(a)

#         visited = set()
#         dfs = [source]

#         while dfs: 
#             top = dfs.pop()
#             visited.add(top)
#             if top == destination:
#                 return True
            
#             for other in adj[top]:
#                 if other in visited:
#                     continue
#                 dfs.append(other)





#         return False


        
        