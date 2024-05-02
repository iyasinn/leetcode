class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        second = -1
        output = ""
        for index, char in enumerate(word): 
            if char == ch: 
                second = index 
                break 

        if second == -1: 
            return word

        return word[second::-1] + word[second + 1::]
        