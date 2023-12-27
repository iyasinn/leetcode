# Sliding window and keep the highest to remove balloon in that sliding window
"""
We can simply keep a total sum, and keep a largest value. And subtract that largest value from the window when possible

"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        start = 0 
        time = 0

        window_time = 0
        window_max = 0

        for end in range(len(colors)): 
            
            if colors[end] == colors[start]: 
                window_time += neededTime[end]
                window_max = max(window_max, neededTime[end])
                continue
            
            time += (window_time - window_max)
            window_time = window_max = neededTime[end]
            start = end

        # This will be zero if start == end    
        time += (window_time - window_max)
        
        return time




            
                    
        