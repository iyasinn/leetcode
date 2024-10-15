"""
Approach: Simulate the zigzag and build it, then return the solution

is there a better way to do this

Some columns will always have stuff in 
Observation

First column
Then every row (numRows + 1) afterwards

So everything modulo class (numRows + 1)
To get th enext item in the row, we know that we will have to go down, then up until we get to that column
Can we calculate how many we have to skip to get this? 

We need to hit all letters for a row
And so we apply the zig zag patter for the row
The number of movments is this

[negative movements] (numRows - rowIndex - 1) + numRow [this is the. ol movement]

(numRows - rowIndex - 1) + numRow 
This tells us how much we can skip to get to the to p

SO numRow - index - 1 movement down, then diagonal, then jump

Then we can do the same thing, but we also have to "jump"
So P -> I -> N -> Out of bounds
Next Row
A 


"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: 
            return s

        rows = [""] * numRows

        r = 0
        d = 1

        for c in s: 
            rows[r] += c

            r += d

            if r == numRows or r == -1: 
                d = d * -1
                r += (d + d)
            
        return "".join(rows)






        # move = 2 * (numRows - 1)
        # cols = floor(len(s) / move)

        # print(cols)

        # return ""
        # currRow = 0

        # output = ""

        # while currRow < numRows:

        #     # Start index is currRow
        #     start_i = currRow

        #     while start_i < len(s): 
        #         output += s[start_i]
        #         start_i += move




        
        