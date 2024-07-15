# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""

Root has no parent elements
Each description tells us what can't be the root 

So that means the root is not a child of anything
So it doesnt appear in child portion
We also know that all children appear once 
Or they appear twice 

set of parents - set of children == root 
but it's a very slow operation 

We could also not do set minus, and jsut consider eac element individually? 
"""

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:



        nodes = {}

        children = set(d[1] for d in descriptions)
        root = None
        

        for d in descriptions: 
            nodes[d[0]] = nodes.get(d[0], TreeNode(d[0]))
            nodes[d[1]] = nodes.get(d[1], TreeNode(d[1]))

            if d[0] not in children: 
                root = d[0]

            if d[2]: 
                nodes[d[0]].left = nodes[d[1]]
            else: 
                nodes[d[0]].right = nodes[d[1]]
        
  
        return nodes[root]