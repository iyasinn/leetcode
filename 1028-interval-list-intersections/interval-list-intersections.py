

"""
Two approaches in ind
Keep mergin A intervals with B, if not working, then move whichever one appears first, and if both appear first, the move one that ends first 


so take a and b, if they inte

OR

We know each is pairwise disjoint

Object slice
Put both into events queue

And whenever b and a are one, we have a new interval
The moment one of them closes, we determine to add 

4 states
n = a + b
n = 0 
n = 1 (something opened)
n = 2 (sometihing opened)

if n goes to 1, then that means somethign closed, so we have to consider that a new interval closure

Hard edge case arrives because we close and get our interval, then what is considered the left bound? 
We keep track of a left bound and b left bound, that is we keep track of which interval opening or closign

NO point doing this because we have sorted list of intervals anyway 

"""




class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        output = []
        f = 0
        s = 0

        while f < len(firstList) and s < len(secondList):
            fS, fE = firstList[f]
            sS, sE = secondList[s]

            start, end = max(fS, sS), min(fE, sE)

            if start <= end:
                output.append([start, end])

            if fE <= sE:
                f += 1
            else:
                s += 1

        return output




        