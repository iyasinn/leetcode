class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for n in arr: 
            freq[n] = freq.get(n, 0) + 1
        return len(set(freq.values())) == len(freq.values())
        