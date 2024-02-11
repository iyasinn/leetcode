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
        curr_min = None

        for end in range(len(s)): 
            window[s[end]] = window.get(s[end], 0) + 1
            while start <= end and subset(window, tFreq):
                if curr_min is None or (end + 1) - start < len(curr_min):
                    curr_min = s[start:end+1]
                window[s[start]] -= 1
                start += 1

        return "" if curr_min is None else curr_min