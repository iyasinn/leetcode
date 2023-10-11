class Solution:




    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = "" 
        firstWord = strs[0]

        for i in range(len(firstWord)):

            letter = firstWord[i]

            for j in range(len(strs)): 
                word = strs[j]
                if len(word) <= i or word[i] != letter: 
                    return prefix 
                    
            prefix += letter
        
        return prefix


            


        