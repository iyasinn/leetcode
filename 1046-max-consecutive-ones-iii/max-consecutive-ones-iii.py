"""

Really just give max array size if you can only have numZero in it 

Lets try simple array slice

Simpler

For any element
If it's a zero, have to solve for k - 1 and prev
Otherwise

prev + k
And keep doing for all elements that end at an index


"""
"""
WHenever you see 1s and 0s, think prefix sum 

"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # prefix = accumulate([0] + nums)


        best = 0
        l = 0 
        zero = 0
        
        for r in range(len(nums)):
            zero += int(nums[r] == 0)
            while l <= r and zero > k:
                zero = zero - 1 if nums[l] == 0 else zero
                l += 1
            best = max(best, r - l + 1)
            r += 1

        return best

            

        