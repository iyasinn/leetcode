

def LCP(a, b): 
    if len(a) > len(b): 
        a, b = b, a
    lcp = ""
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]: 
            break
        lcp += a[i]
    return lcp

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        done = False
        lcp = strs[0]
        for s in strs: 
            lcp = LCP(lcp, s)
        return lcp
        