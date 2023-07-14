# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (not root): 
            return 0
        elif (not root.right and not root.left):
            return 1

        answer = float('inf')

        if (root.right):
            answer = min(answer, self.minDepth(root.right))
        if (root.left):
            answer = min(answer, self.minDepth(root.left))
        
        return 1 + answer

        
    


