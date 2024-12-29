"""

Array
Need to maximize the sightseeing

a[i] + a[j] + (j - i)

Maximizing a[i] and a[j] is easy, can do through a sorting 

I feel a greedy would help here

For any specific element, we need to compare it to best
But then what's the ealirest? 

We can actually havae two ealierests
One by j, and one by size? 


8 1 5 2 6

see 1, 1 + 8 + 1 = 10
THen we go to 5, now 5 it is better for it to stay at 8 

The moment we see a larger number than our start, we can just move our left pointer there

Only edge case

Actually what we wnat is farhter 
THis is really asking? 
Farthest largest pair kidn of 
Distance gives more priority kind of 
But smaller sum can have such a large distance it makes up for it



3 0 0 0 0 4 0 0 10

So maybe we consider the distance and we update our current by that disnace

8 1 8 2 10

Bst pair is 8 + 10 + 2 = 20

8 is left, then 9 vs 1, then 10 vs 15 -> 15 is better
Now lets see if 


"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        i = 0
        best = float('-inf')

        for j in range(1, len(values)):
            curr = values[i] + values[j] + (i - j)
            best = max(best, curr)

            if values[i] + (i - j) < values[j]:
                i = j 
        
        return best
            



        