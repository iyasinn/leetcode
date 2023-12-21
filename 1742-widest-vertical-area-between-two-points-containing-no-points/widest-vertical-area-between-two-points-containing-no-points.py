class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        points.sort()
        best = 0

        for i in range(len(points) - 1):
            area = points[i + 1][0] - points[i][0]
            best = max(best, area)
        
        return best
        