@cache
def dp(n, k, target, curr): 
    MODULO = ((10 ** 9) + 7)

    if n == 0: 
        return int(target == curr)
    elif n > 0 and curr >= target: 
        return 0
    
    ways = 0 
    for i in range(1, min(k, target - curr) + 1):
        ways += dp(n - 1, k, target, curr + i)
    
    return ways % MODULO

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return dp(n, k, target, 0)


        