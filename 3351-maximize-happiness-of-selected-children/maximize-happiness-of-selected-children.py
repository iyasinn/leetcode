"""
0:00 - understanding
choose k children in k turns, where we pick one child per turn 

each pick, all non picked children happiness decreases by 1 until 0 

need maximum sum of selecting k children 

[1, 2, 3]
k = 2 

it would be wisest to greedily select the largest children

"""




class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum([max(0, happiness[i] - i) for i in range(k)])