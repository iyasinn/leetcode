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

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        best = 0
        l = 0 
        r = 0
        zero = 0

        while r < len(nums):

            if nums[r] == 0:
                zero += 1

            while l <= r and zero > k:
                zero = zero - 1 if nums[l] == 0 else zero
                l += 1
            best = max(best, r - l + 1)
            r += 1

        return best

            

        