"""
O(n^2) brute force
For each spot see if you can reach the end

Now, we need to reduce this somehow

AN array slice precomputation seems nice
That is
Is there something we can cmopute about the array to make this easier 




gas
[2, 3, 4]

For 2, we know how much gas will be needed to get baack to two? 
sum of all costs to do RT

During the journey you have gas[i] you can use to fill up your tank 
This seems like producer consumer

Each part has a threshold. We consume some, or gain some 
So for index 0, 

2, and 3
WE produce 2, and consume 3, so we are at -1

Which means we need at least 1 in the tank when we get to 1



cost = 
[3, 4, 3]


SO we know the delta of each index, how much we need

So now it's a matter of does our delta ever drop below 0. If it does,
 that's our new start? 

[2, 3, 4] gas
[3, 4, 3] cost

[-1, -1, 1]
start at 0, cant do it, move over, cant do it, move over, start here, then try to do a roudn trip
and eventually we can't do it cuz we cant reach back 

So left and right pointer, and try to do a round trip? 
"""


def add_one(val, size):
    return (val + 1) % size

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        delta = [gas[i] - cost[i] for i in range(n)]

        start = 0 
        end = 0
        curr = 0

        # So end is not before start
        while add_one(end, n) != start:

            curr += delta[end]

            while start <= end and curr < 0: 
                curr -= delta[start]
                start = add_one(start, n)

            end = add_one(end, n)

            if start == 0 and end == 0: 
                return -1
        
        return start if curr + delta[end] >= 0 else -1


        