class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = {}
        for n in nums: 
            freq[n] = freq.get(n, 0) + 1
        
        output = []
        
        for k, v in freq.items(): 
            if v > (len(nums) // 3): 
                output.append(k)
        
        return output

        