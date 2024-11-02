# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

4(2(3)(1))(6(5))

stack 
push 4 on 

4 (call str2)

Add a ( at the start and end )

And then the subproblem is that we start with a ()

4 (2(3)(1)) (6(5))
"""

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        if len(s) == 0: 
            return None


        rootStr = ""

        for i in range(len(s)):
            if s[i] in "()":
                break
            rootStr += s[i]
        
        root = TreeNode(int(rootStr))

        opens = 0
        start = i + 1

        for end in range(i, len(s)):
            if s[end] == "(":
                opens += 1
            elif s[end] == ")":
                opens -= 1
            if opens == 0:
                break

        root.left = self.str2tree(s[start:end])

        if end + 1 >= len(s) or s[end + 1] == ")":
            return root
        root.right = self.str2tree(s[end + 2:len(s) - 1])

        return root







