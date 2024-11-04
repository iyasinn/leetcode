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

def intersect(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        output = []

        for s, e in intervals:
            if newInterval and newInterval < [s, e]:
                output.append(newInterval)
                newInterval = None
            if output and intersect(output[-1], [s, e]):
                output[-1] = [min(output[-1][0], s), max(output[-1][1], e)]
            else:
                output.append([s, e])

            if newInterval and intersect(newInterval, output[-1]):
                output[-1] = [min(output[-1][0], newInterval[0]), max(output[-1][1], newInterval[1])]
                newInterval = None


        if newInterval: 
            output.append(newInterval)

        return output
        