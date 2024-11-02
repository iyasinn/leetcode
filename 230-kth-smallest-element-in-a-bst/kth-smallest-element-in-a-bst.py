# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    

        dfs = [root]

        while True: 

            top = dfs.pop()

            if top.left:
                dfs.append(top)
                dfs.append(top.left)
                top.left = None
                continue

            k -= 1

            if 0 == k: 
                return top.val 

            if top.right: 
                dfs.append(top.right)

        return None
            


        # def dfs(root):
        #     nonlocal sol
        #     nonlocal curr

        #     if root == None: 
        #         return
            
        #     left = dfs(root.left)
        #     curr += 1

        #     if curr == k: 
        #         sol = root.val
        #         return

        #     right = dfs(root.right)
        
        # dfs(root)
        # return sol



        