# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
inorder traversal? no ordering in binary tree
traversal and keep track of max element along the way? If curr element is larger than max, then we have an issue
cant sovle this through recursion of subproblem because we car eabout the previous roots


"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, hi):
            if root is None: 
                return 0
            
            total = 1 if root.val >= hi else 0
            hi = max(root.val, hi)
            total += dfs(root.left, hi)
            total += dfs(root.right, hi)
            return total
        return dfs(root, root.val)

        