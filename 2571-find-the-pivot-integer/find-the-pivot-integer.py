class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot_sum = 0
        total = (n * (n + 1)) // 2
        # pivot_sum is sum[1, pivot]
        
        for pivot in range(1, n + 1):
            pivot_sum += pivot
            if pivot_sum == (total - pivot_sum + pivot):
                return pivot 
        
        return -1
        