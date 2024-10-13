
"""
Each list is sorted in non decreasing order (can have the same element)
Need smallest range

So given all of these

What if we tried some sort of pointer movement approah
Let's think about how we can decrease a range

1
2
3

Given this, the range must be [smallest, largest]

So given that we know for any set of numbers, whats the smallest and largest (we could use a pq)

Can we optimize? 

Which element to move? 
If we wanna make the range smaller, then I'm guessing you want the range to get smaller by moving the smallest one up by one
And see this new range

4 10 15 24 26
0 9 12 20 
5 18 22 30

[4, 0, 5] -> [0, 5]
Move 0
[4, 9, 5] -> [4, 9]
Move 4
[10, 9, 5] -> [5, 10]

We can keep doing until we get to [20, 24] which has a size of 4 

So really, we're finding the smallest range
Our invariant is that all numbers are in it
Decrease range size by moving smallest number up

Now how to figure out which number is smallest / largest? 
Manually calculate largest

Hvae a min pq of all numbers and their index 

get smallest, and get largest
then after movng smallest you can update largest if needed if new number is larger than current number

The largest cant be moved

"""

import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        largest = max(row[0] for row in nums)
        pq = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(pq)

        best = [float('-inf'), float('inf')]

        while pq: 
            smallest, row, col = pq[0]
            heapq.heappop(pq)

            if (largest - smallest) < (best[1] - best[0]): 
                best = [smallest, largest]
            
            if col + 1 == len(nums[row]): 
                break


            if nums[row][col + 1] > largest: 
                largest = nums[row][col + 1]
            
            heapq.heappush(pq, (nums[row][col + 1], row, col + 1))
        
        return best



        