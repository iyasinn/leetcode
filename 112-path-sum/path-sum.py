# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Just a dfs traversal, not really postorder/preorder I think
def dfs(root, currSum, targetSum):
    if (not root): 
        return False

    currSum += root.val
    
    if (not root.left and not root.right):
        return currSum == targetSum
    
    return dfs(root.left, currSum, targetSum) or dfs(root.right, currSum, targetSum)

class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return dfs(root, 0, targetSum)