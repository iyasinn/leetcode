class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        output = []

        # lower needs to be included

        for n in nums: 
            if n > lower: 
                output.append([lower, n - 1])
                lower = n + 1
            elif n == lower:
                lower += 1
        
        if lower <= upper:
            output.append([lower, upper])
        
        return output


        