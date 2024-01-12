class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        for i in range(len(s) // 2): 
            count += (s[i] in "aeiouAEIOU")
            count -= (s[(len(s) // 2) + i] in "aeiouAEIOU")

        return count == 0