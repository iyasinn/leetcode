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
    
        currNode = None

        if root1 and root2: 
            currNode = root2
            currNode.val += root1.val
            print(currNode.val)
            currNode.left = self.mergeTrees(root1.left, root2.left)
            currNode.right = self.mergeTrees(root1.right, root2.right)

            return currNode

        if root2 is None: 
            root1, root2 = root2, root1
        
        currNode = root2 
        currNode.left = self.mergeTrees(None, root2.left)
        currNode.right = self.mergeTrees(None, root2.right)

        return currNode

        




        # if root1: 
        #     currNode = root1
        # if ro
        