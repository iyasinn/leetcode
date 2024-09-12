class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0 
        for s in words: 
            if set(s).issubset(set(allowed)): 
                count += 1

        return count