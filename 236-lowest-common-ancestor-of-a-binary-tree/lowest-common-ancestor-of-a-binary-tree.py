# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.euler = []
        self.pIndex = None
        self.qIndex = None
        
        def dfs(root, depth):
            if root is None: 
                return
            
            dfs(root.left, depth + 1)

            self.euler.append((root, depth))

            if p == root: 
                self.pIndex = len(self.euler) - 1
            elif q == root:
                self.qIndex = len(self.euler) - 1

            dfs(root.right, depth + 1)

        dfs(root, 0)
        pI, qI = min(self.pIndex, self.qIndex), max(self.pIndex, self.qIndex)

        bestDepth, ans = float('inf'), None
        while pI <= qI:
            val, depth = self.euler[pI]
            if depth < bestDepth:
                ans = val
                bestDepth = depth
            pI += 1
        
        return ans













        # if root is None:
        #     return None

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # # So root is the ancestor, and we find something in left or right
        # if root in [p, q] or (left and right):
        #     return root
        # return left or right
        