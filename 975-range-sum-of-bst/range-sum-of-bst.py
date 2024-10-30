# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Dont need to go left at a certain point




class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        curr = 0
        
        if root.val >= low:
            curr += self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            curr += self.rangeSumBST(root.right, low, high)

        if low <= root.val <= high:
            curr += root.val

        return curr
            
        