"""
We could use a priority queue that contains all the elements
Pop largest element, add, and then push it back 

But interestingly, we know that how each number is going to go down 


Keep using largest element
We do know how each element will change though 

But priority queue seems easiest

"""

import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        pq = [n * -1 for n in nums] # Max heap
        heapq.heapify(pq)

        total = 0
        print(nums)
        print(pq)

        for _ in range(k): 
            val = heapq.heappop(pq)
            total += (val * -1)
            heapq.heappush(pq, math.floor(val / 3))
        
        return total


        