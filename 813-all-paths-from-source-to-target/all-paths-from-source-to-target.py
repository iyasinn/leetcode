"""
0:00
We are given a graph that is a list matrix representation of how we can approach the problem. 
We need to keep track of our current solution as we traverse through the graph and likely keep it somehwere in some form of shared state 


Need to review backtrackig notes on leetcode 

"""


def backtrack(graph, curr_path, solution, index): 
    if index == len(graph) - 1: 
        solution.append(curr_path[0::])
        return

    for next_index in graph[index]: 
        curr_path.append(next_index)
        backtrack(graph, curr_path, solution, next_index)
        curr_path.pop()
    

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        solution = []
        backtrack(graph, [0], solution, 0)
        return solution