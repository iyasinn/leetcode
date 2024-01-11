# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Return min, max, diff
"""

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root): 
            if not root.left and not root.right: 
                return root.val, root.val, 0
            diff = 0
            top_min = root.val
            top_max = root.val

            for subtree in (root.left, root.right): 
                if not subtree: 
                    continue
                tree_min, tree_max, tree_diff = dfs(subtree)
                top_min = min(top_min, tree_min)
                top_max = max(top_max, tree_max)
                diff = max([diff, abs(tree_min - root.val), abs(tree_max - root.val), tree_diff])

            return top_min, top_max, diff
        
        if not root: 
            return 0
        return dfs(root)[2]