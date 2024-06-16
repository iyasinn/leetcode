"""
Reading the problem, I understand what it's asking but it's confusing
- Can I simplify this to a small example 
- To what extent can I determine if a number can be formed

Doing brute force may be simplest right now 
How do I determine if a number can be formed? 
I could go through all combinations of numbers 
Then find the closest number and add that 
But it doesn't seem very efficient 

So I would first explore the tree to see what can be formed 
Then I would try to add numbers from there 

1, 5, 10 

"""


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        current_max = 1 
        count = 0 

        i = 0
        while current_max <= n: 
            # Adding anything in this range guarantees
            # That we can form (2 * current_max) + 1, or whatever new sum we get
            if i < len(nums) and nums[i] <= current_max: 
                current_max += nums[i]
                i += 1
            else: 
                current_max += current_max 
                count += 1

        return count
        