from collections import defaultdict
import itertools 
  
# import operator to work  
# with operator 
import operator 
  
# creating a list GFG 
GFG = [1, 2, 3, 4, 5] 
  
# using the itertools.accumulate()  
result = itertools.accumulate(GFG,  
                              operator.mul) 

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = defaultdict(int)
        for start, end in intervals: 
            events[start] += 1
            events[end + 1] -= 1
        
        max_overlaps = max(itertools.accumulate([events[t] for t in sorted(events)]))
        return max_overlaps

