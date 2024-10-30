class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        

        l, r, i = m - 1, n - 1, len(nums1) - 1

        while r >= 0: 
            if l >= 0 and nums1[l] > nums2[r]:
                nums1[i] = nums1[l]
                l -= 1
            else:
                nums1[i] = nums2[r]
                r -= 1
            i -= 1

        return nums1 


        l = m - 1
        r = n - 1

        i = len(nums1) - 1

        while l >= 0 and r >= 0: 
            if nums1[l] > nums2[r]:
                nums1[i] = nums1[l]
                i -= 1
                l -= 1
            else:
                nums1[i] = nums2[r]
                i -= 1
                r -= 1
        
        while l >= 0: 
            nums1[i] = nums1[l]
            i -= 1
            l -= 1


        while r >= 0:
            nums1[i] = nums2[r]
            i -= 1
            r -= 1

        return nums1

        # O(nlogn), O(1) space
        nums1[m::] = nums2
        nums1.sort()
        