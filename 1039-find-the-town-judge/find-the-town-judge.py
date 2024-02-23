class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        freq = {num: 0 for num in range(1, n + 1)}

        for a, b in trust: 
            if a in freq: 
                freq.pop(a)
            if b in freq: 
                freq[b] += 1
        
        print(freq)

        found = -1

        for key, val in freq.items(): 
            if val == n - 1 and found == -1: 
                found = key 
            elif val == n - 1: 
                return False
        
        return found
        