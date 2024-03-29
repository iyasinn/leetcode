class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        freq = [0] * (n + 1)
        freq[0] = -1

        for a, b in trust: 
            freq[a] -= 1
            freq[b] += 1
        
        if freq.count(n - 1) == 1: 
            return freq.index(n - 1)
    
        return -1
        