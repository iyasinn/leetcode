"""
We simply need to see if each character is divisibly by the number of words
"""

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charFreq = {}
        for word in words: 
            for char in word: 
                charFreq[char] = charFreq.get(char, 0) + 1
        
        for freq in charFreq.values(): 
            if freq % len(words) != 0: 
                return False

        return True
        

        