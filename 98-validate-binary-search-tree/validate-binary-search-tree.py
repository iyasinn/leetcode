# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
First idea. Just do inorder traversal! 
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev = float('-inf')
        valid = True

        def dfs(root):
            nonlocal prev
            nonlocal valid
            if root is None: 
                return True

            left = dfs(root.left)

            if root.val <= prev:
                return False

            prev = root.val 
            right = dfs(root.right)
        
            return left and right

        return dfs(root)

        # def dfs(root, lo, hi):
        #     if root is None: 
        #         return True
            
        #     if root.val <= lo or root.val >= hi: 
        #         return False
            
        #     left = dfs(root.left, lo, root.val)
        #     right = dfs(root.right, root.val, hi)
        #     return left and right
        
        # return dfs(root, float('-inf'), float('inf'))

            
            

        