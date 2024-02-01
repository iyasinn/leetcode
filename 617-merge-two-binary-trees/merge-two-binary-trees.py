# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 is None and root2 is None: 
            return None
    
        merged_node = TreeNode()

        root1 = root1 if root1 else TreeNode()
        root2 = root2 if root2 else TreeNode()
        merged_node.val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        merged_node.left = self.mergeTrees(root1.left, root2.left)
        merged_node.right = self.mergeTrees(root1.right, root2.right)
        return merged_node

        




        # if root1: 
        #     currNode = root1
        # if ro
        