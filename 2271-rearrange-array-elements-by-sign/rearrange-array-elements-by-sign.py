class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 0
        output = []

        while (len(output) < len(nums)):
            if len(output) % 2 == 0: 
                while nums[pos] < 0: 
                    pos += 1
                output.append(nums[pos])
                pos += 1
            elif len(output) % 2 == 1:
                while nums[neg] > 0: 
                    neg += 1
                output.append(nums[neg])
                neg += 1 
                
        return output

    # def rearrangeArray(self, nums: List[int]) -> List[int]:
    #     pos = [n for n in nums if n > 0]
    #     neg = [n for n in nums if n < 0]
    #     output = []
    #     for i in range(len(pos)): 
    #         output += [pos[i], neg[i]]
    #     return output
