class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = {}
        for start, end in intervals: 
            events[start] = events.get(start, 0) + 1
            events[end + 1] = events.get(end + 1, 0) - 1
        
        max_intervals = 0
        curr = 0 

        for time in sorted(events): 
            delta = events[time]
            curr += delta

            if curr > max_intervals: 
                max_intervals += (curr - max_intervals)
        
        return max_intervals
            