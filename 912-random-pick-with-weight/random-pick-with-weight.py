import random
import bisect


"""

0 - 1 - 4

1 - 2 - 4



"""


class Solution:
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.w = list(accumulate(w))
        
    def pickIndex(self) -> int:

        num = random.randint(1, self.total)
        index = bisect.bisect_left(self.w, num)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()