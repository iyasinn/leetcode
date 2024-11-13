class Solution:

    def __init__(self, nums: List[int]):
        self.m = defaultdict(list)
        for i, n in enumerate(nums): 
            self.m[n].append(i)

    def pick(self, target: int) -> int:
        array = self.m[target]
        index = random.randint(0, len(self.m[target]) - 1)
        return self.m[target][index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)