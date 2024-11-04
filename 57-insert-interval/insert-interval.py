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
        # Treat newInterval as currInteral
        output = []
        for s, e in intervals: 
            print(newInterval)
            if e < newInterval[0]:
                output.append([s, e])
            elif s > newInterval[1]:
                output.append(newInterval)
                newInterval = [s, e]
            else:
                nS, nE = min(s, newInterval[0]), max(e, newInterval[1])
                newInterval = [nS, nE]
        output.append(newInterval)
        return output


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []
#         for interval in intervals:
#             if interval[1] < newInterval[0]:
#                 res.append(interval)
#             elif interval[0] > newInterval[1]:
#                 res.append(newInterval)
#                 newInterval = interval
#             else:
#                 newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
#         res.append(newInterval)
#         return res

            # So we are after newInterval
            # Before new Interavl
            # Or we overlap





        