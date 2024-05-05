class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        end = 0

        letters = set()
        best = 0

        while end < len(s):

            if end < len(s) and s[end] in letters: 
                letters.remove(s[start])
                start += 1
                continue

            letters.add(s[end])
            best = max(len(letters), best)
            end += 1

        return best

        