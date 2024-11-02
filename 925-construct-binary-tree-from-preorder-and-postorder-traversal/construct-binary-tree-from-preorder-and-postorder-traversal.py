# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""

all unique values
pre order will print all the values of the left tree first
post order will also print all the values of the left tree 
we know first elmenet of preorder is root
so find where the root ends up being in the post order, and thats the end boundary 



pre: 1,     2, 4, 5, |  3, 6, 7
post:       4, 5, 2, |  6, 7, 3,      1

This it te boundary of the left tere and the right tree. 
WHat gives away this boundary? 

Need to figure out what is on left side of tree, and what is on rihgt side of tree with a given roo t
"""
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        if len(pre) == 0:
            return None
        if len(pre) == 1: 
            return TreeNode(pre[0])

        root = TreeNode(pre[0], None, None)

        pre.pop(0)
        post.pop()

        leftEnd = post.index(pre[0]) + 1

        left = self.constructFromPrePost(pre[0:leftEnd], post[0:leftEnd])
        right = self.constructFromPrePost(pre[leftEnd:], post[leftEnd:])

        root.left = left
        root.right = right

        return root





        