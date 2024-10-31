# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(root):
            if root is None: 
                return None, 0
            
            left, leftCount = dfs(root.left)
            right, rightCount = dfs(root.right)

            # If root is a value we want
            if root in nodes:
                return root, leftCount + rightCount + 1
            elif left and right:
                return root, leftCount + rightCount
            
            # Now root is definitely not a ancestor because it doesnt have split or count
            return left or right, leftCount + rightCount

        curr, count = dfs(root)
        # if count != len(nodes): 
        #     return None
        return curr