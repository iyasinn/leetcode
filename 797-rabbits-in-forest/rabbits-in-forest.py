class Solution:
    # def numRabbits(self, answers: List[int]) -> int:

    #     freq = {}
    #     total = 0

    #     for num in answers: 

    #         total += 1

    #         if num in freq and freq[num] > 0: 
    #             freq[num] -= 1
    #         else: 
    #             freq[num] = num 

    #     for num in freq.values():
    #         total += num
        
    #     return total

    # Fastest in terms of runtime
    def numRabbits(self, answers: List[int]) -> int:

        freq = {}
        total = 0

        # Essentially we dont wanna see duplicates
        for num in answers: 
            if num in freq and freq[num] > 0: 
                freq[num] -= 1
            else: 
                freq[num] = num 
                total += num + 1
    

        return total


    # Greedy algorithm, from Dev
    # def numRabbits(self, answers: List[int]) -> int:

    #     freq = {}
    #     total = 0

    #     for num in answers: 
    #         freq[num] = freq.get(num, 0) + 1

    #     for key, val in freq.items():
    #         total += ceil(val / (key + 1))  * (key + 1)
         

    #     return total

