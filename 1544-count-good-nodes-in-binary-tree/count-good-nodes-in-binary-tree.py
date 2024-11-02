# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None: 
            return 0 

        best = 0 

        def dfs(root, high):
            nonlocal best
            if root is None:
                return 0
            if root.val >= high: 
                best += 1
            
            dfs(root.left, max(high, root.val))
            dfs(root.right, max(high, root.val))
        
        dfs(root, float('-inf'))
        return best