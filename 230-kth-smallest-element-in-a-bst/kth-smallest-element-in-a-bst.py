# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        sol = 0
        curr = 0 

        def dfs(root):
            nonlocal sol
            nonlocal curr

            if root == None: 
                return 0
            
            left = dfs(root.left)
            curr += 1

            if curr == k: 
                sol = root.val

            right = dfs(root.right)
        
        dfs(root)
        return sol



        