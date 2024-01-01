"""
We could do this with a pq
minheap of cookies, and minHeap of children
Or sorting
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gI, sI = 0, 0
        count = 0

        while sI < len(s) and gI < len(g): 
            if s[sI] >= g[gI]: 
                count += 1
                sI += 1
                gI += 1
            else: 
                sI += 1

        return count