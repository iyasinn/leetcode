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
        if not root: 
            return 0

        def dfs(root): 
            if not root.left and not root.right: 
                return root.val, root.val, 0


            diff = []
            top_min = root.val
            top_max = root.val

            if root.left: 
                left_min, left_max, left_diff = dfs(root.left)
                top_max = max(top_max, left_max)
                top_min = min(top_min, left_min)
                diff += [abs(root.val - left_min), abs(root.val - left_max), left_diff]
            if root.right: 
                right_min, right_max, right_diff = dfs(root.right)
                top_max = max(top_max, right_max)
                top_min = min(top_min, right_min)
                diff += [abs(root.val - right_min), abs(root.val - right_max), right_diff]


            return top_min, top_max, max(diff)
        
        return dfs(root)[2]