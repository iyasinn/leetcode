# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        minpq = []
        bfs = [root]

        while bfs:

            level_size = len(bfs)
            level_val = 0

            for _ in range(level_size): 
                node = bfs.pop(0)
                level_val += node.val
                if node.left:
                    bfs.append(node.left)
                if node.right: 
                    bfs.append(node.right)
            
            heappush(minpq, level_val)
            if len(minpq) > k: 
                heappop(minpq)
        
        return minpq[0] if len(minpq) == k else -1
                
                
                
