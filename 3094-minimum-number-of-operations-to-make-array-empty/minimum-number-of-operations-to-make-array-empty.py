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

3k -> k operations
3k + 1
k - 1 3s, and a 2

3k + 2
k 3s, and a 2


How to moe every number ot 3

For any number n, itr is going to be  ceil(n / 3)

Prrof that T(n) = ceil(n / 3)

T(2) = 1
T(3) = 1

ceil(n / 3)




"""



class Solution:
    def minOperations(self, nums: List[int]) -> int:

        freq = {}
        for num in nums: 
            freq[num] = freq.get(num, 0) + 1

        moves = 0
        
        for key, count in freq.items(): 
            if count != 1: 
                moves += ((count + 2) // 3)
            else: 
                return -1
        return moves