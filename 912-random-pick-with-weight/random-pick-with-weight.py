import random
import bisect




class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.w = list(accumulate(w))
        
    def pickIndex(self) -> int:

        # Literally picking a random integer so remember that!
        num = random.randint(0, self.total - 1)
        index = bisect.bisect_right(self.w, num)
        return index

        # num = random.randint(1, self.total)
        # index = bisect.bisect_left(self.w, num)
        # return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()