class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]
        output = []
        for i in range(len(pos)): 
            output += [pos[i], neg[i]]
        return output
