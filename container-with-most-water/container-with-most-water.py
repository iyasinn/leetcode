class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        best = 0

        while (left < right):
            if (height[left] <= height[right]):
                best = max(best, height[left] * (right - left))
                left += 1
            else:
                best = max(best, height[right] * (right - left))
                right -= 1
        
        return best