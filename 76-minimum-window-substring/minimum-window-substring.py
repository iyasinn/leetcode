# O(|W|) comparison to see if window fits the substring

def subset(window, tFreq):
    for key in tFreq.keys():
        if key not in window or window[key] < tFreq[key]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tFreq = Counter(t)
        start = 0 
        window = {}
        best_start, best_end = -1, 10000000

        for end in range(len(s)): 
            window[s[end]] = window.get(s[end], 0) + 1
            while start <= end and subset(window, tFreq):
                if (end + 1) - start < (best_end + 1) - best_start:
                    best_start, best_end = start, end
                window[s[start]] -= 1
                start += 1


        return "" if best_start == -1 else s[best_start:best_end+1]