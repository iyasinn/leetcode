def next_pos(start, nums):
    while start < len(nums) and nums[start] < 0: 
        start += 1
    return start

def next_neg(start, nums): 
    while start < len(nums) and nums[start] > 0: 
        start += 1
    return start
    

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = next_pos(0, nums)
        neg = next_neg(0, nums)

        output = []

        for _ in range(len(nums) // 2): 
            output += [nums[pos], nums[neg]]
            pos = next_pos(pos + 1, nums)
            neg = next_neg(neg + 1, nums)

        return output

    # def rearrangeArray(self, nums: List[int]) -> List[int]:
    #     pos = [n for n in nums if n > 0]
    #     neg = [n for n in nums if n < 0]
    #     output = []
    #     for i in range(len(pos)): 
    #         output += [pos[i], neg[i]]
    #     return output
