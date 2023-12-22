"""
0:00
Reading problem statement

Score is number of 0s in left + number of 1's in right
Since we care about a count in a range, we could simply do two O(N) loops
One to get number of 0s until an index
Another to get number of 1s until an index from right ot left
Prefix and postfix, we can find the points, and then select the max points

3:31
Realize we need to be careful with out split
For each score index, we assume that the index is pert of the right substring
We need a dummy index so that all indexes can be part of the left substring


5:09 
GO through test case


011101


30:00
Realized the best method is to simply consider all the substrings. There will always be a left and a right portion, so we can simply just consider that


"""

class Solution:
    def maxScore(self, s: str) -> int:
        # Assume all the 1's are in the right, and we have zero 0's in the left
        num_zero = 0
        num_one = s.count('1')
        best_score = -1

        for i in range(len(s) - 1):
            num_zero += (1 if s[i] == '0' else 0)
            num_one  += (-1 if s[i] == '1' else 0)
            best_score = max(best_score, num_zero + num_one)

        return best_score