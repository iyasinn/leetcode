"""

Jumped into the solution too fast = bad
Mathematically there does seem to be a select form here
Maybe proof by induction can posit the truth for this? 


1 -> -1
2 -> 1
3 -> 1

4 -> 2
5 -> 2
6 -> 2

7 -> 3


How to moe every number ot 3

For any number n, itr is going to be  ceil(n / 3)




"""



class Solution:
    def minOperations(self, nums: List[int]) -> int:

        freq = {}
        for num in nums: 
            freq[num] = freq.get(num, 0) + 1

        moves = 0
        print(freq)

        for count in freq.values(): 
            if count == 2 or count == 3: 
                moves += 1
            elif count > 3: 
                moves += ceil(count / 3)
            else: 
                return -1
        return moves