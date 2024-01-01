"""
We could do this with a pq
minheap of cookies, and minHeap of children
Or sorting
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count, size_index = 0, 0
        while count < len(g) and size_index < len(s): 
            if s[size_index] >= g[count]: 
                count += 1
                size_index += 1
            else: 
                size_index += 1

        return count