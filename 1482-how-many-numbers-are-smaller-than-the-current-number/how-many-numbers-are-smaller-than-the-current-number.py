class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Last spot bucket[101] = 0 in all situations, essential for base case bucket[0]
        bucket = [0] * 102
        for n in nums: 
            bucket[n] += 1
        for i in range(101):
            bucket[i] += bucket[i - 1]   
        return [bucket[n - 1] for n in nums]



# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         freq = Counter(nums)
#         for i in range(101):
#             freq[i] += freq[i - 1]   
         
#         for i in range(len(nums)): 
#             nums[i] = freq[nums[i] - 1]
#         return nums 
       