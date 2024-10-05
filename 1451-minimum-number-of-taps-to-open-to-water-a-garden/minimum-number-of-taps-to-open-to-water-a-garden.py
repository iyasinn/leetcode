import pprint




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

        for i in range(1, n + 1):

            if i > curr and farthest_next == -1: 
                return -1
            
            if i in m: 
                farthest_next = max(farthest_next, m[i])
            
            if i >= curr: 
                print("next farthest:", curr, farthest_next)
                curr = farthest_next
                farthest_next = -1
                count += 1
            
            if curr == n: 
                return count
            elif farthest_next == n: 
                return count + 1


        return -1