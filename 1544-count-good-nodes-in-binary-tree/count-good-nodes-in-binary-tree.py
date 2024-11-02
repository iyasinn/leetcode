# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None: 
            return 0 

        stack = [(root, root.val)]
        count = 0

        while stack: 
            top, prevHigh = stack.pop()
            if top.left: 
                stack.append((top.left, max(prevHigh, top.val)))
            if top.right:
                stack.append((top.right, max(prevHigh, top.val)))
            
            if top.val >= prevHigh:
                count += 1
                
        return count



        def dfs(root, high):
            if root is None:
                return 0
            
            total = 1 if root.val >= high else 0
            total += dfs(root.left, max(high, root.val))
            total += dfs(root.right, max(high, root.val))
            return total

        
        return dfs(root, float('-inf'))
