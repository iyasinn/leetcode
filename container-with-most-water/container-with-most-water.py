class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        start = 0
        end = len(height) - 1

        while start < end:

            res = max(res, min(height[start], height[end]) * (end - start))

            if (height[start] < height[end]):
                start += 1
            else: 
                end -= 1
        
        return res
