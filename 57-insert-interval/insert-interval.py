"""
We have two arrays
So we are inserting new intervals
In my head object slicing is verysimple for this
As long as we are > 1 we have an interval
Object slicing is chill


OR


Take interval
If an intersection, then we add it, but that intersection might cause new overlaps
and those new overlaps might then need to be considered

We only have one new interval
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        events = defaultdict(int)

        for s, e in (intervals + [newInterval]):
            events[s] += 1
            events[e] -= 1 

        curr = 0

        output = []

        for key in sorted(events):
            if curr == 0 and curr + events[key] > 0:
                output.append([key, None])
            elif curr > 0 and curr + events[key] == 0:
                output[-1][1] = key
            elif curr == 0 and curr + events[key] == 0:
                output.append([key, key])
            curr += events[key]

        return output




        