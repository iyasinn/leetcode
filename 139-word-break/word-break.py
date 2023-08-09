class Solution:

    # If we can find a good recurrenc erelation 
    # Find number of words that end with the current word 

    def dp(self, s, index, wordDict, memo): 

        if (index < 0): 
            return True
        if (memo[index] != None): 
            return memo[index]

        found = False 
        
        for word in wordDict: 
            if index + 1 - len(word) < 0: 
                continue 

            currString = s[index + 1 - len(word): index + 1]

            if (currString == word): 
                found = self.dp(s, index - len(word), wordDict, memo)

            if found: 
                break

        memo[index] = found
        return memo[index]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None] * len(s)
        return self.dp(s, len(s) - 1, wordDict, memo)







