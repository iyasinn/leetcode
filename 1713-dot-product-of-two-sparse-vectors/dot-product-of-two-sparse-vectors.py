class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indices = set([i for i in range(len(nums)) if nums[i] > 0])

        # Since it's mostly 0s, what if we stored indices that arent 0 then in O(1) time used those
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:


        indices = set(self.indices).intersection(vec.indices)
        total = 0
        
        for i in indices:
            total += (self.nums[i] * vec.nums[i])
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)