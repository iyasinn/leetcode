class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        """
            Need to get from start to end minimally

        """

        m = defaultdict(int)
        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = i + ranges[i]
            m[start] = max(end, m[start])
        
        curr = 0
        farthest = 0 
        taps = 0

        for i in range(n):
            if i in m:
                farthest = max(farthest, m[i])
                
            if i == curr:
                curr = farthest
                farthest = 0 
                taps += 1
            
        if curr >= n: 
            return taps
        return -1
            





        