class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        solution = -1
        freq = {}
        for i, char in enumerate(s): 
            freq[char] = freq.get(char, i)
            solution = max(solution, i - freq[char] - 1)
        return solution 







        