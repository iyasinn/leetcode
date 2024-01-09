# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rec(root, seq): 
    if root is None: 
        return 
    
    rec(root.left, seq)
    rec(root.right, seq)

    if root.left is None and root.right is None:
        seq.append(root.val)
    
    return seq

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return rec(root1, []) == rec(root2, [])