class Solution:

    def rec(self, candidates, target, currTarget, currSol, sol, i):
        if i < 0: 
            return
        if currTarget > target: 
            return

        # Don't include current 
        self.rec(candidates, target, currTarget, currSol, sol, i - 1)

        currTarget += candidates[i]
        currSol.append(candidates[i])

        if currTarget == target: 
            sol.append(currSol.copy())
        else: 
            # Include current and then also try again for current
            self.rec(candidates, target, currTarget, currSol, sol, i)
        
        currTarget -= candidates[i]
        currSol.pop()
        return
    

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        currSol = []
        self.rec(candidates, target, 0, currSol, sol, len(candidates) - 1)
        return sol
        