"""
I tried to do some recursive approach 
I'm struggling because not certain how the cases relate


All submatrix is O(n^2)

ruel of prefix
rP - lP = sum of middle 

1 2 3 
1 3 6
6 - 1 = 5 which is sum exlucing 1

Let's say we have prefix sums across all rows
now at any element, we can either serch for the next part of the row 

Hint: This has show men that a sum of a matrix can be found in O(1) using prefix sums

For each element, we can now find the size of the matrix as needed


Innovation: dont' need to select r, c, r2, c2
can do 
r, r2, then the c's are actually constant c's, your selecting noe c 


could select r, c, r2, 

n^3

"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        count = 0
        n = len(matrix)
        m = len(matrix[0])
        prefix = [list(accumulate([0] + row)) for row in matrix]

        # [start, end] inclusive
        for col_start in range(m):
            for col_end in range(col_start, m): 

                seen = defaultdict(int)
                row_prefixes = [prefix[row][col_end + 1] - prefix[row][col_start] for row in range(n)]

                for pre in accumulate([0] + row_prefixes): 
                    count += seen[pre - target]
                    seen[pre] += 1

        return count

"""
1 -1 
-1 1



                    while row_start <= row_end and curr > target:
                        curr -= prefix[row_start][col_end + 1] - prefix[row_start][col_start]
                        row_start += 1

                    if row_start <= row_end and curr == target:

"""



        
        



        