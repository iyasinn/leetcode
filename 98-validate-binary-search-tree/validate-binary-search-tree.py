# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, lo, hi):
            if root is None: 
                return True
            
            if root.val <= lo or root.val >= hi: 
                return False
            
            left = dfs(root.left, lo, root.val)
            right = dfs(root.right, root.val, hi)
            return left and right
        
        return dfs(root, float('-inf'), float('inf'))

            
            

        