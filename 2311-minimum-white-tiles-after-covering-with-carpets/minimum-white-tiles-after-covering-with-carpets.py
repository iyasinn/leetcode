
"""

0:00
0-indexed binary string
0 is black, 1 is white
we have numCarpets of length carpetLen, these are black
Need to minimize the number of white tiles

To me, it would seem that we need to take all subsets and cover them
Can we count up all substrings of white, and then work with them?

Observation: Cannot individually consider each substring. Because some lengths of carpet might overlap and cover multiple substrings of whtie carpets. Maybe we could linearly include the distance between two substrings, and then consider the carpet cover length of that? 

1:01
We also can't only consider tiles with the largst length. Consider 
111000000001010101
And a carpet length of size 7, and 1 of them. Then this needs to cover the right end. Not the left end.
Observation: Can't consider a greedy algorithm 

2:02
Conclusion: Consider dp 
Approach: We can place a carpet, retreat x steps back and retreat length_black_carpet steps, and count carpets along the way. For each tile, we place a carpet, or we don't. 
Optimal substructure? Yes. Breaking teh problem down, reducing one of our carpet sizes, lets us work with elss carpets. 

3:37
T(n, num_carpets) = 
If white: min(1 + T(n - 1, num_carpets), T(n - carpet_length, num_carpets - 1))
If black: T(n - 1, num_carpets)

4:50
Begin implementation


13:06
Something wrong. Can't pass all cases
Forgot to check if numCarpets is greater than 0 when calling numCarpet

"""

class Solution:

    def __init__(self): 
        self.carpetLen = 0

    def dp(self, floor, index, numCarpets, memo): 
        if (index, numCarpets) in memo: 
            return memo[(index, numCarpets)]
        elif index < 0: 
            return 0

        if floor[index] == '0':
            return self.dp(floor, index - 1, numCarpets, memo)
            
        no_place = self.dp(floor, index - 1, numCarpets, memo) + 1
        place_carpet = no_place

        if numCarpets > 0: 
            place_carpet = self.dp(floor, index - self.carpetLen, numCarpets - 1, memo)

        memo[(index, numCarpets)] = min(no_place, place_carpet)
        return memo[(index, numCarpets)] 
        

    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        self.carpetLen = carpetLen
        memo = {}
        return self.dp(floor, len(floor) - 1, numCarpets, memo)
