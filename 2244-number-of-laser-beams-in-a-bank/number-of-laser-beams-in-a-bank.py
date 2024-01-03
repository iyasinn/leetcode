"""
We have beam locatons
On each row we have beams
And now to map any two beams together, we simply need to see if they are compatible
We could satrt at any beam and then look at every other row, and stop, but this seems inefficient
Given a beam on a row...we know that each beam on that row is reproducible, their outcome will be the same, aka ()beamA * connections ) * numBeeams on that row
After that we need to go through other rows, and simply check
We can do this in O(n^2)

It kind of reminds me of dp 

dp(row) = count(security) * num_security(prev) + prev

"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        numBeams = 0
        prev_count = 0

        for row in range(len(bank)): 
            curr_count = bank[row].count('1')
            if curr_count > 0: 
                numBeams += (prev_count * curr_count)
                prev_count = curr_count
        
        return numBeams
        