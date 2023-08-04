class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freq = {}
        total = 0

        for num in answers: 
            
            total += 1

            if num in freq and freq[num] > 0: 
                freq[num] -= 1
            else: 
                freq[num] = num 

        for num in freq.values():
            total += num
        
        return total

