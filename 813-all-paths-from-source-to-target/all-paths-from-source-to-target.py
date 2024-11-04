"""
It's directed and acycicl so we dont need a visited matrix

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        curr = []
        output = []

        def dfs(i):
            nonlocal curr
            nonlocal output
            if i == len(graph) - 1:
                output.append(curr.copy())
                return

            for n in graph[i]:
                curr.append(n)
                dfs(n)
                curr.pop()
        
        curr = [0]
        dfs(0)

        return output
