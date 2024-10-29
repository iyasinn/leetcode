"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set([None])
        while p is not None: 
            visited.add(p)
            p = p.parent
        
        while q is not None: 
            if q in visited:
                return q
            q = q.parent

        return None