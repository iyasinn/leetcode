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
    

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        seq1 = []
        seq2 = []
        rec(root1, seq1)
        rec(root2, seq2)

        # print(seq1)
        # print(seq2)

        return seq1 == seq2