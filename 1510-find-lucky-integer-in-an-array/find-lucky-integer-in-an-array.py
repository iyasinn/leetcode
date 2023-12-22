class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr: 
            freq[num] = freq.get(num, 0) + 1
        
        
        for key, val in reversed(sorted(freq.items())): 
            if key == val: 
                return key

        return -1