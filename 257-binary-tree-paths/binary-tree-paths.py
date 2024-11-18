# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None: 
            return None

        
        oldSize = len(self.curr)

        if len(self.curr) > 0:
            self.curr += "->"
        self.curr += str(node.val)

        if not node.left and not node.right:
            self.sol.append(self.curr)
            self.curr = self.curr[0:oldSize]
            return

        self.dfs(node.left)
        self.dfs(node.right)
        self.curr = self.curr[0:oldSize]
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.sol = []
        self.curr = ""

        self.dfs(root)
        return self.sol
        
