# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: 
            return []

        m = {}
        bfs = [(root, 0)]

        while bfs:
            node, col = bfs.pop(0)
            if col not in m:
                m[col] = []
            m[col].append(node.val)
            if node.left:
                bfs.append((node.left, col - 1))
            if node.right:
                bfs.append((node.right, col + 1))
        
        return [m[key] for key in sorted(m)]



        