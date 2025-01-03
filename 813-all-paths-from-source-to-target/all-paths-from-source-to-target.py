"""
It's directed and acycicl so we dont need a visited matrix

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(i):
            if i == len(graph) - 1:
                self.output.append(self.curr.copy())
                return

            for n in graph[i]:
                self.curr.append(n)
                dfs(n)
                self.curr.pop()
        
        self.curr = [0]
        self.output = []
        dfs(0)
        return self.output
