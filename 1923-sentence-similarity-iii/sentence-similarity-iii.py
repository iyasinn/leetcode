

def match(s1, s2, l, r): 
    return s1[l] == s2[l] and s1[r] == s2[r]

class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:

        section = 1
        s1 = s1.split()
        s2 = s2.split()

        if len(s2) < len(s1): 
            s1, s2 = s2, s1
        elif len(s1) == len(s2): 
            return s1 == s2
        

        i = 0 
        while i < len(s1) and s1[i] == s2[i]: 
            i += 1
        # now we are at an i where s1[i] != s2[i]
        # now see if [i, len(s1)] is equivalent to s2 - len(s1)

        for x in range(len(s1) - i):
            if s1[len(s1) - x - 1] != s2[len(s2) - x - 1]:
                return False
    
        return True
    
                



        