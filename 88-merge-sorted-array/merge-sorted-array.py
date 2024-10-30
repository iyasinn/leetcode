class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        

        # Find the n largest elements, and fill the array, then backfill 



        # O(n) two pointer, O(n) space
        temp = []
        l = 0
        r = 0 

        while l < m or r < n:
            if l < m and r < n:
                if nums1[l] < nums2[r]:
                    temp.append(nums1[l])
                    l += 1
                else:
                    temp.append(nums2[r])
                    r += 1
                continue
            if l < m: 
                temp.append(nums1[l])
                l += 1
            else:
                temp.append(nums2[r])
                r += 1
        
        for i in range(len(temp)):
            nums1[i] = temp[i]
        return nums1

        # O(nlogn), O(1) space
        nums1[m::] = nums2
        nums1.sort()
        