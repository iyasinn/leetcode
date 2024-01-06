"""
If we consider every time entry that finishes <= curr_start time
Then we can simply say that we need start at the beginning of a interval
And then consider all intervals that come before this beginning interval 
But also if we have an interval that doesn't intersect, we could just consider it nontrivially
It depends on start time clearly

How do we get next intervals in this ordering
20 -> go thru all remainign ones and make sure next start is after the current end



---


Looks like LIS wherfe start1 <= end1 <= start2 <= end2 I feel 




"""




"""
If we consider every time entry that finishes <= curr_start time
Then we can simply say that we need start at the beginning of a interval
And then consider all intervals that come before this beginning interval 
But also if we have an interval that doesn't intersect, we could just consider it nontrivially
It depends on start time clearly

How do we get next intervals in this ordering
20 -> go thru all remainign ones and make sure next start is after the current end



The issue with the LIS approach is that we don't want O(n^2) to keep iterating through the array. We cant make our problem ENDING at an index
We have to make including or excluding

"""




# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         data = [(startTime[i], endTime[i], profit[i]) for i in range(len(profit))]
#         data.sort(key=lambda x: (x[1], x[0]))

#         print(data)

#         @lru_cache
#         def rec(index): 
#             if index == -1: 
#                 return 0
            
#             curr_start, curr_end, curr_profit = data[index]
#             max_profit = 0

#             # Need a faster way to find a job that iterating slowly through 
#             last_element = bisect.bisect_left(data, curr_start, key=lambda x: x[1]) + 1
            
#             for i in range(last_element, -1, -1): 
#                 if i < 0 or i >= len(data): 
#                     break
#                 group = data[i]
#                 start, end, _ = group

#                 if end <= curr_start: 
#                     max_profit = max(rec(i), max_profit)
#                 else:
#                     break
            
#             max_profit += curr_profit
#             return max_profit
            
#         return max(rec(i) for i in range(len(data)))


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = [(startTime[i], endTime[i], profit[i]) for i in range(len(profit))]
        data.sort(key=lambda x: x[1])

        print(data)

        @lru_cache
        def rec(index): 
            if index == -1: 
                return 0
            
            curr_start, curr_end, curr_profit = data[index]
            max_profit = 0

            last_element = bisect.bisect_right(data, curr_start, key=lambda x: x[1]) - 1
            include_curr = rec(last_element) + curr_profit
            exclude_curr = rec(index - 1)

            return max(include_curr, exclude_curr)
            
        return rec(len(profit) - 1)