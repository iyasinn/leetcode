

"""

1 0 0
0 1 1 
0 1 1

0 1 1
0 1 1 
0 1 1

all 1s

is there every a case where we need to do a columh flip
then row flip? 

it seems we can always do either way 
row and column
so im arguing that a row flip and column flip does not need any order
A bood way to prove is if we can get the results of a column flip
and a row flip in any order 

given n moves, with m row flips
we know that we have n chose m different ways to play the move
for each row, it will experience a consistent number of flips

better approach
let's assume we flip row 0, then column 0 
then now assume we flip column 0, then row 0 

in both cases the first grid[0][0] experiences two flips, the remaining experience 1 flip on row 0 and column 0 
So ordering does not matter 


Finally, do we need to do multiple passes? 
We should be able to optimize immediately

Assuming we optimize the number of 1s in a row 
Then we assume that all 1s are near the start, to get the largest number
That is due to binary representation, 
We must end up with a 1 at position 0 
becuase sum of all digits after first digit in binary 
will just give us one less than the nth digit
sum i=1-n of 2^n digit in binary = 2^n

so nth digit is always 1
so if first digit is not 1, we then do a flip of that row 
then we go through columns and we make sure we can flip columns
to maximize their score


0 1 0
1 0 1 
1 0 1

proof by contradiction
assume if there are more 0s than 1s, we don't need to flip a row 
wrong
because you can do a flip, and then since you have same row or same column
then you now have more 0s than 1s
"""

def flip(grid, row=None, col=None):
    if row is not None and col is not None: 
        assert(False)

    if row is not None: 
        for c in range(len(grid[0])): 
            grid[row][c] ^= 1
    else: 
        for r in range(len(grid)): 
            grid[r][col] ^= 1



class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)): 
            if grid[row][0] == 0: 
                flip(grid, row, None)

        for col in range(len(grid[0])): 
            num_zero = [grid[row][col] for row in range(len(grid))].count(0)
            if num_zero > len(grid) - num_zero: 
                flip(grid, None, col)
        
        total = 0 
        for row in grid: 
            total += int("".join(str(x) for x in row), 2)

        return total 



        return 3