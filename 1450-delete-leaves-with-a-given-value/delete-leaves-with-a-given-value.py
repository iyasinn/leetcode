# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        if root is None: 
            return None 

        def helper(root): 
            if root is None: 
                return None
            if root.left is None and root.right is None: 
                return root
            
            helper(root.left)
            helper(root.right)

            if root.left and root.left.left is None and root.left.right is None and root.left.val == target: 
                root.left = None
            if root.right and root.right.left is None and root.right.right is None and root.right.val == target: 
                root.right = None 
            
            return root 
        
        val = helper(root)
        if val.left is None and val.right is None and val.val == target: 
            return None 
        return val 
        
