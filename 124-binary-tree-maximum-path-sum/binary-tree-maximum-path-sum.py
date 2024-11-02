# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# This reminds me of prefix sum 
# 2^n paths
# Branch and bound could be used potentially 
# TO do an efficent dfs 
# But path does not need to pass from root, and it can go up and down 

# Some we could convert this to a graph bprolbme
# Add parent nodes

# At eac n

"""

But at each node, I see two potential ideas

At each given node, I can do two things 

I can start a new path and go left or right


I can take the left path and go to the right
Or I can take the right path and go ot the left 

The best path on the left does not necessarily intersect with the element at the left

However, I could have an invarient that it does actually end at each node

Why? 

For the example 
9 we end with 9 
for the -10, let us first see what ends at 20 

15 ends at 15, 7 ends at 7

summing everythign for 20 is valuable, so we get 37
Whiel doing this we can keep track of the best in a variable of its own 
"""



class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0

        def dfs(root): 
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            curr = max([root.val, left + root.val, right + root.val])
            self.best = max([self.best, curr, left + right + root.val])
            return curr

            
        self.best = root.val
        dfs(root)
        return self.best



        