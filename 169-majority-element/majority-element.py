class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        best = nums[0]
        for n in nums: 
            if n != best: 
                count -= 1
            else: 
                count += 1
            if count == 0: 
                best = n
                count = 1
        return best