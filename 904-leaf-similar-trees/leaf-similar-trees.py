# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rec(root, seq, remove=False): 
    if root is None: 
        return 
    
    rec(root.left, seq, remove)
    rec(root.right, seq, remove)

    if root.left is None and root.right is None:
        if remove and len(seq) > 0 and root.val == seq[-1]: 
            seq.pop()
        else: 
            seq.append(root.val)
    
    return seq

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        seq = []
        rec(root1, seq)
        seq = seq[::-1]
        rec(root2, seq, True)

        print(seq)

        return len(seq) == 0