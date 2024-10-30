# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = root

        def dfs(root):
            nonlocal ans
            if root is None: 
                return False

            isAnc = root in [p, q]

            left = dfs(root.left)
            right = dfs(root.right)

            if isAnc and (left or right):
                ans = root
            elif left and right:
                ans = root

            return isAnc or left or right

        dfs(root)
        return ans






        if root is None:
            return None

        print(root or root)

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root in [p, q]: 
            return root
        if (left and right):
            return root
        return left or right
        