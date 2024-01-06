"""
If we consider every time entry that finishes <= curr_start time
Then we can simply say that we need start at the beginning of a interval
And then consider all intervals that come before this beginning interval 
But also if we have an interval that doesn't intersect, we could just consider it nontrivially
It depends on start time clearly

How do we get next intervals in this ordering
20 -> go thru all remainign ones and make sure next start is after the current end


"""




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