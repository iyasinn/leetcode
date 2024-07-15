# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        nodes = {}

        root = set(d[0] for d in descriptions)
        

        for d in descriptions: 
            nodes[d[0]] = nodes.get(d[0], TreeNode(d[0]))
            nodes[d[1]] = nodes.get(d[1], TreeNode(d[1]))

            root -= set([d[1]])

            if d[2]: 
                nodes[d[0]].left = nodes[d[1]]
            else: 
                nodes[d[0]].right = nodes[d[1]]
            
        
        return nodes[list(root)[0]]