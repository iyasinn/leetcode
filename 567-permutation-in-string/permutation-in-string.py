class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        curr = Counter(s2[0:len(s1)])

        if freq == curr: 
            return True

        for i in range(len(s1), len(s2)): 
            curr[s2[i]] += 1
            curr[s2[i - len(s1)]] -= 1

            if freq == curr: 
                return True

        return False
        
        