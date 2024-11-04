# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# def valid(data, level):
#     tup = (0, len(data) - 1, 1 if level % 2) == 0 else (len(data) - 1, 0, -1)
#     start, end, direction = 

#     for i in 



class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode], level=0) -> bool:

        odd = False
        bfs = [root]

        while bfs: 
            size = len(bfs)
            last = float('inf') if odd else float('-inf')

            for i in range(size): 
                front = bfs.pop(0)
                mult = -1 if odd else 1
                if last * mult >= front.val * mult:
                    return False
                if front.val % 2 == odd:
                    return False
                last = front.val
                if front.left:
                    bfs.append(front.left)
                if front.right:
                    bfs.append(front.right)
            odd = False if odd else True
        return True
                







        