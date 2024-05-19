
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


"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        num_open = 0 
        curr = []
        solution = []

        def dfs(pair): 
           
            nonlocal curr
            nonlocal solution 
            print(pair, curr)
            nonlocal num_open

            # check if solution
            if pair == n and num_open == 0:
                solution.append("".join(curr))
                return
            
            # Two different types of promising. Check them both
            # Then generate next solution

            # Can add a )
            if num_open > 0: 
                curr.append(')')
                num_open -= 1
                dfs(pair)
                num_open += 1
                curr.pop()

            # Can add a (
            if pair < n: 
                curr.append('(')
                num_open += 1
                dfs(pair + 1) 
                num_open -= 1
                curr.pop()
        
        dfs(0)
        return solution
            



        
        