"""

0:00
10^4 unique integers
What if we created an array of size 10^4
Then we worked on a prefix and a postfix sum
O(10^4) to create, O(n) fill in though 

O(n) to calculate prefix
Furthermore prefix tells you the postfix implicitly becuase we have a max size here 
Is prefix and postfix inclusive?


so if i have a value
and there are 3 people behind me, so 4 is my prefix
but there are 8 people total 
then I have 4 people ahead of me 
So my psoition is 5th 

Perhaps I should have calculated postfix instead, exclusive

then there are 



1, 0, 1, 1, 0, 1
            1  0


postfix[i] = postfix[i + 1] + value[i + 1]

Prefix and postfix bucket sort was slow because of large constant size
Using an index method was much faster

"""

def position(n):
    temp = [None, "Gold", "Silver", "Bronze"] 
    return temp[n] + " Medal" if n <= 3 else str(n)

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        mapping = {score[i]: i for i in range(len(score))}
        
        for i, key in enumerate(sorted(mapping.keys(), reverse=True)): 
            score[mapping[key]] = position(i + 1)

        return score



