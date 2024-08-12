class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(ord(x) - 48 for x in bin(n)[2::])

        