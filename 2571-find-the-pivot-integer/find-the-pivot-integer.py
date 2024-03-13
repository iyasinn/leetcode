class Solution:
    def pivotInteger(self, n: int) -> int:
        for p in range(1, n + 1):
            if (p * (p + 1)) // 2 == (((n * (n + 1)) // 2) - ((p * (p - 1)) // 2)):
                return p 
        return -1




