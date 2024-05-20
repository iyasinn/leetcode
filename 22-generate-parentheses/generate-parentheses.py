
"""
Know it's a brute force because we need all well formed parentheses
We can describe a well formed parentheses using a dfs search space

The search space will end if we have valdi parentheses at the end
We know we need to use exactly all n parentheses 

At any step, we can: add a new ( if possible, or add a ), then add a ( if possible. 
Or add a ), and add a (, or we could add multiple ) 

So instead, at any step 
we can 

m = number of ) 

T(n, m) = T(n - 1, m) + T(n, m + 1)

We can only have m == number of placed ( and only if it possible to do so
We can do this with a simple nmber

We can make ourselves have a count 

T(leftCount, rightCount, pair)

So when leftCount == rightCount and pair == n: 



"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        num_open = 0 
        solution = []


        def dfs(pair, left, right): 
        
            nonlocal solution

            # check if solution
            if len(pair) == (n * 2) and left == right: 
                solution.append(pair)
                return
        
            if left > right:  
                dfs(pair + ')', left, right + 1)
            if left < n: 
                dfs(pair  + '(', left + 1, right)
        
        dfs("", 0, 0)
        return solution
            



        
        