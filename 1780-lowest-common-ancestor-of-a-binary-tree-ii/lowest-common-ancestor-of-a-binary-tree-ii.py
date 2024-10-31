# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Find LCA but it needs to exist 
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if root is None: 
                return None, 0
            
            left, leftCount = dfs(root.left, p, q)
            right, rightCount = dfs(root.right, p, q)

            # If root is a value we want
            if root in [p, q]:
                return root, leftCount + rightCount + 1
            elif left and right:
                return root, leftCount + rightCount
            
            # Now root is definitely not a ancestor because it doesnt have split or count
            return left or right, leftCount + rightCount

        curr, count = dfs(root, p, q)
        if count != 2: 
            return None
        return curr

    


        


        