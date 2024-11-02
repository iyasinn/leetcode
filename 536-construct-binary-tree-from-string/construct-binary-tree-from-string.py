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

def get_num(s, i):
    num = ""
    for c in s[i:]:
        if c in "()":
            break
        num += c
    return num, i + len(num)

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        def dfs(s, i):

            rootNum, i = get_num(s, i)

            if len(rootNum) == 0: 
                return None, i + 1


            rootNum = int(rootNum)
            root = TreeNode(rootNum)

            if i >= len(s) or s[i] == ")":
                return root, i + 1
            
            if s[i] == "(":
                root.left, i = dfs(s, i + 1)

            if i < len(s) and s[i] == "(":
                root.right, i = dfs(s, i + 1)
            
            return root, i + 1
        
        a, b = dfs(s, 0)
        return a
        
       





