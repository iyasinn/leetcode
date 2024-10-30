class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        

        # Find the n largest elements, and fill the array, then backfill 



        # O(n) two pointer, O(n) space
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

        # temp.extend(nums1[l:m])
        # temp.extend(nums2[r:])

        # print(temp)
        

        return nums1

        # O(nlogn), O(1) space
        nums1[m::] = nums2
        nums1.sort()
        