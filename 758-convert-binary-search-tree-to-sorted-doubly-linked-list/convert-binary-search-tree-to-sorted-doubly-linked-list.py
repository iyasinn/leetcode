"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

"""

This feels like a euler tour problem
1 -> 2 -> 3 -> 4 -> 5

Inorder traversal gets us the euelr tour we need

"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: 
            return None

        eulerPath = []

        def dfs(root):
            nonlocal eulerPath
            if root is None: 
                return

            dfs(root.left)
            eulerPath.append(root)
            dfs(root.right)
        
        dfs(root)

        head = eulerPath[0]
        for i, node in enumerate(eulerPath):
            nextNode = eulerPath[i + 1] if i + 1 < len(eulerPath) else eulerPath[0]
            prevNode = eulerPath[i - 1] if i - 1 >= 0 else eulerPath[-1]

            node.left = prevNode
            node.right = nextNode

        return head






        
        