# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

4(2(3)(1))(6(5))
stack 
push 4 
4 (call str2)
Add a ( at the start and end )
And then the subproblem is that we start with a ()
4 (2(3)(1)) (6(5))
"""

def getNumber(s, ptr): 
    out = ""

    while ptr < len(s):
        if s[ptr] in "()":
            break
        out += s[ptr]
        ptr += 1
    return out, ptr


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        s = list(s)
        
        if len(s) == 0: 
            return None
        

        firstNum, i = getNumber(s, 0)
        stack = [TreeNode(int(firstNum))]
        head = stack[0]

        while i < len(s):
            c = s[i]
            if c in "(":
                i += 1
                continue
            elif c in ")":
                i += 1
                stack.pop()
                
            
            num, i = getNumber(s, i)

            if num == "": 
                continue

            num = int(num)

            node = TreeNode(num)

            if stack[-1].left:
                stack[-1].right = node
            else:
                stack[-1].left = node
            
            stack.append(node)
        
        return head







