# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def dfs(root):
            if root is None: 
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)

            # If root is a value we want
            if root in nodes:
                return root
            elif left and right:
                return root
            
            # Now root is definitely not a ancestor because it doesnt have split or count
            return left or right

        curr = dfs(root)
        return curr