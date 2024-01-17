class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for n in arr: 
            freq[n] = freq.get(n, 0) + 1
        
        bucket = set()

        for key, count in freq.items(): 
            if count in bucket: 
                return False 
            bucket.add(count)
        
        return True
        