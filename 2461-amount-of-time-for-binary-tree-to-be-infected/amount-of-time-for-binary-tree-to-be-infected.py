# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}
        infected_start = None

        def dfs(node):
            nonlocal parents
            nonlocal infected_start
            if node == None: 
                return 
            
            if node.left: 
                parents[node.left] = node
                dfs(node.left)
            if node.right: 
                parents[node.right] = node 
                dfs(node.right)
            if node.val == start: 
                infected_start = node 
 
        dfs(root)
        max_time = 0
        visited = set([infected_start])
        bfs = [(infected_start, 0)]

        while len(bfs) > 0: 
            node, curr_time = bfs.pop()
            max_time = max(max_time, curr_time)

            if node in parents and parents[node] and parents[node] not in visited: 
                bfs.append((parents[node], curr_time + 1))
                visited.add(parents[node])
            if node.left and node.left not in visited: 
                bfs.append((node.left, curr_time + 1))
                visited.add(node.left)
            if node.right and node.right not in visited: 
                bfs.append((node.right, curr_time + 1))
                visited.add(node.right)
        
        return max_time







        

