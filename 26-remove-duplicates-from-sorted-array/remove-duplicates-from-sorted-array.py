class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        prev = None
        
        for num in nums: 
            if num != prev:
                nums[ptr] = prev = num
                ptr += 1
  
        return ptr


        