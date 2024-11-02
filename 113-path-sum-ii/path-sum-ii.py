# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Need all paths means generate all paths
This means that we nee dto actually go thorugh an genrate
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def builder(root):
            if root is None:
                return

            self.currPath.append(root.val)
            self.currSum += root.val

            if not root.left and not root.right and self.currSum == targetSum:
                self.sol.append(self.currPath.copy())
                
            builder(root.left)
            builder(root.right)

            self.currPath.pop()
            self.currSum -= root.val
            return
        
        self.currSum = 0
        self.currPath = []
        self.sol = []

        builder(root)
        return self.sol

        
