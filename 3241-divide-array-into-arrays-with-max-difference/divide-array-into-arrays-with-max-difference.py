"""
0:00
We need the differnece between some element and any other element to be less than k

Given n1, n2, n3
Can it be the case that we should grpu n1 and n3 instead of n1 and n2
I argue no if we sort our solution
We could also maybe bucket sort as an O(n) sort but we can try approaching that a bit later 

will try the sort method 
condition 1: one or more arrays of size 3
condition 2: each elementin only one array 
condition 3: the diff of any two elements is less than or equal to k

"""


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0: 
            return []
        nums.sort()
        output = []

        for i in range(0, len(nums), 3):
            output.append([nums[i], nums[i + 1], nums[i + 2]])
            if abs(max(output[-1]) - min(output[-1])) > k: 
                return []
        
        return output
