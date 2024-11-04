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
            curr.append(i)

            if i == len(graph) - 1:
                output.append(curr.copy())
                curr.pop()
                return

            for n in graph[i]:
                dfs(n)

            curr.pop()
        
        dfs(0)
        return output
