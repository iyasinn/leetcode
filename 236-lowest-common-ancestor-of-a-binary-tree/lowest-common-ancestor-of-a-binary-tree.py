# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Simpel approach in head
Get the path twoards p
Then get the path towards q. And as you get the path to q, keep updating the common ancesotr you find
Until you find q
Because lowest common ancestor will also be the one that is closest to q
"""

import copy

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pathP = []
        currPath = []
        
        best = None
        anc = root

        def dfsP(root):
            nonlocal pathP
            nonlocal currPath
            if not root:
                return
            if root == p:
                pathP = currPath.copy()
                return
            
            for node in [root.left, root.right]:
                if node:
                    currPath.append(node)
                    dfsP(node)
                    currPath.pop()
        
        dfsP(root)

        if q in pathP:
            return q

        def dfsQ(root):
            nonlocal anc
            nonlocal best
            if not root: 
                return 

            if root == q:
                print("ANC")
                print(anc.val)

                best = anc
                return

            oldAnc = anc
            if root in pathP:
                anc = root
            
            dfsQ(root.left)
            dfsQ(root.right)
            anc = oldAnc



        dfsQ(root)



        return best

