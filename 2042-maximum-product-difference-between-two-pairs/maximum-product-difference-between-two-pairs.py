
"""


observation: Product difference not commutative. diff(A, B) != diff(B, A)

The max difference is most definitely the largest (a * b) subtracted by the smallest (c * d)
Take the two largest numbers, and the two smallest numbers 

"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])