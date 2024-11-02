class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, prev):
            if root is None: 
                return True, prev

            # Traverse the left subtree
            left_is_valid, left_prev = dfs(root.left, prev)
            if not left_is_valid:
                return False, left_prev
            
            # Check current node with the "prev" value from the left subtree
            if left_prev is not None and root.val <= left_prev:
                return False, root.val

            # Traverse the right subtree with the current root's value as the new "prev"
            return dfs(root.right, root.val)

        is_valid, _ = dfs(root, None)
        return is_valid
