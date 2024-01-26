class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        for i in(range(101)):
            freq[i] += freq[i - 1]

        for i in range(len(nums)): 
            nums[i] = freq[nums[i] - 1]

        return nums 



        