from collections import defaultdict

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = defaultdict(int)
        for start, end in intervals: 
            events[start] += 1
            events[end + 1] -= 1
        
        max_overlaps = 0
        curr_overlaps = 0 

        for time in sorted(events): 
            delta = events[time]
            curr_overlaps += delta
            max_overlaps = max(curr_overlaps, max_overlaps)
        
        return max_overlaps
            