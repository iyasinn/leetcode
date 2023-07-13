# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The depth of any given node is the depth of the parent node + the depth of the curren tnode
# The depth of the root node is 1
# So really, I'd say we need to keep a running track of the largest possible node
# When looking at some node, we can honestly keep calculating the running depth
# And find another way to store the best depth
# This seems like another DFS, so I will map it to that
# We will try returning the best depth possible

class Solution:



    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if (not root):
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
