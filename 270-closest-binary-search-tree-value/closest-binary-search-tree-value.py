# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def closer(a, b, target):
    a, b = min(a, b), max(a, b)
    if abs(a - target) <= abs(b - target): 
        return a
    return b

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None: 
            return float('inf')

        optimal = None

        if root.val < target:
            optimal = self.closestValue(root.right, target)
        elif root.val > target:
            optimal = self.closestValue(root.left, target)
        else: 
            return root.val
        
        optimal = closer(root.val, optimal, target)

        return optimal


        