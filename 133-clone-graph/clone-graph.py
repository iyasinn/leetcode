"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
I don't want to move backwards
But an easy approach to this is that we only move to large neighbors


"""

from typing import Optional
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        self.visited = {None: None}

        def clone(node):
            if node in self.visited:
                return

            copy = Node(node.val)
            self.visited[node] = copy

            for n in node.neighbors:
                if n in self.visited:
                    copy.neighbors.append(self.visited[n])
                else:
                    clone(n)
                    copy.neighbors.append(self.visited[n])
            
        
        clone(node)
        return self.visited[node]



        