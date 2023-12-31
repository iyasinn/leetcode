class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        solution, freq = -1, {}
        for i, char in enumerate(s): 
            solution = max(solution, i - (freq.setdefault(char, i)) - 1)
        return solution 







        