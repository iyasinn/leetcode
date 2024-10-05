class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        m = {}
        for i in range(n + 1): 
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            if start not in m: 
                m[start] = end
            else: 
                m[start] = max(m[start], end)
        
        farthest_next = -1
        curr = m[0]
        count = 1

        for i in range(1, n + 2):

            if i > curr and farthest_next == -1: 
                return -1
            
            if i in m: 
                farthest_next = max(farthest_next, m[i])
            
            if i >= curr: 
                curr = farthest_next
                farthest_next = -1
                count += 1
            
            if curr == n: 
                return count

        return -1



