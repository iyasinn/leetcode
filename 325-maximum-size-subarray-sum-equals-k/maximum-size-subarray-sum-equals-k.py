

"""

0  1, 2, 3, 
0  1  3  6



"""

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix = list(accumulate(nums))
        m = {}
        m[0] = -1
        best = 0

        for i in range(len(prefix)):
            need = prefix[i] - k

            if need in m: 
                best = max(i - m[need], best)
            if prefix[i] not in m:
                m[prefix[i]] = i
        
        return best
        
            
        