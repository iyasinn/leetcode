# With binary search, we might need log(n)

"""

IF k >= n, then k 


Start at n / 2
If k breaks, we have k - 1 eggs and need to solve for superEggDrop(k - 1, n / 2  - 1)

If k doesnt break, then we have k eggs, and we need to go up 
But really, we're solving for superEggDrop (k, n / 2 - 1) because we're solivng for the upper half 

if you have 1 egg, you have to go top down from right to left

If you have more than 1 egg, you can opitmize
You can go in the middle and see if it breaks 



"""

class Solution:
    def __init__(self):
        self.dp = {}

    def superEggDrop(self, k: int, n: int) -> int:
        # Base cases
        if k == 1:  # If you have 1 egg, you must try every floor
            return n
        if n == 0:  # No floors means no drops
            return 0
        
        # Check if result is already computed
        if (k, n) in self.dp:
            return self.dp[(k, n)]

        # Initialize variables
        low, high = 1, n
        result = float('inf')

        # Binary search to minimize the worst case number of drops
        while low <= high:
            mid = (low + high) // 2
            
            # Two scenarios: egg breaks or egg does not break
            egg_breaks = self.superEggDrop(k - 1, mid - 1)
            egg_doesnt_break = self.superEggDrop(k, n - mid)
            
            # Worst case for the current drop
            worst_case = 1 + max(egg_breaks, egg_doesnt_break)

            # We want to minimize the worst-case number of drops
            result = min(result, worst_case)

            # Adjust search space based on the results
            if egg_breaks > egg_doesnt_break:
                high = mid - 1
            else:
                low = mid + 1
        
        # Store result in dp to avoid recomputation
        self.dp[(k, n)] = result
        return result


# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         if k == 1:
#             # Now you have only one possible strategy, to go from top to bottom 
#             return n
#         if n == 0: 
#             return 0

        
#         # Now we assume k > 1 
#         # So now we can try the break in middle strat as much as poss

#         mid = (1 + n) // 2
#         top = n - mid

#         # if drop at n / 2 and breaks, i am too high
#         a = 1 + self.superEggDrop(k - 1, mid - 1)

#         # doenst break at n // 2, so go to the upper levels
#         b = 1 + self.superEggDrop(k, top)

#         return max(a, b)