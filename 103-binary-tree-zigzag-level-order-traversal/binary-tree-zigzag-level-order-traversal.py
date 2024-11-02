# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
            return []

        flip = 1
        output = []
        bfs = [root]

        while bfs: 
            output.append([node.val for node in bfs[::flip]])
            flip *= -1

            size = len(bfs)
            for _ in range(size):
                node = bfs.pop(0)

                if node.left: 
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

        return output

