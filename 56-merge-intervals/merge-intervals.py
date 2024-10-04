def overlap(first, second): 
    return first[1] >= second[0]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True)
        output = []

        print(intervals)


        while len(intervals) > 1:
            if overlap(intervals[-1], intervals[-2]): 
                first = intervals.pop()
                second = intervals.pop()
                new = [first[0], max(first[1], second[1])]
                intervals.append(new)
            else: 
                output.append(intervals[-1])
                intervals.pop()


        if len(intervals) == 1: 
            output.append(intervals[-1])
        
        return output
