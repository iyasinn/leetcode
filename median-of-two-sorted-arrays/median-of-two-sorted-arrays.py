class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        join = nums1 + nums2
        join.sort()
        SIZE = len(join)
        if (len(join) % 2 == 0):
            return (join[SIZE // 2] + join[(SIZE // 2) - 1]) / 2
        return join[SIZE // 2]
        