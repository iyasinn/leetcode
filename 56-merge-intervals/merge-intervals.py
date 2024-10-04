def overlap(first, second): 
    return first[1] >= second[0]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        output = []
        
        for start, end in intervals:
            if not output or output[-1][1] < start: 
                output.append([start, end])
            elif overlap(output[-1], [start, end]):
                output[-1][1] = max(output[-1][1], end)
            
        return output