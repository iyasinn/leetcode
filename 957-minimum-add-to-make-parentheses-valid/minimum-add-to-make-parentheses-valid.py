class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        openn = 0 
        moves = 0

        for c in s:
            if c == "(":
                openn += 1
            elif c == ")" and openn == 0:
                moves += 1
            elif c == ")":
                openn -= 1


        return moves + openn
        