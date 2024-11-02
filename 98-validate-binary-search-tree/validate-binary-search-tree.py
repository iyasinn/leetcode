class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None: 
                return True
        
            if not dfs(root.left):
                return False
            if root.val <= self.prev: 
                return False
            self.prev = root.val
            return dfs(root.right)

        self.prev = float('-inf')
        return dfs(root)
