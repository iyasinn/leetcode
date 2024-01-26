class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        bucket = [0] * 101
        for i in range(len(bucket)):
            bucket[i] = freq[i - 1] + bucket[i - 1]

        for i in range(len(nums)): 
            nums[i] = bucket[nums[i]]
        return nums 



        