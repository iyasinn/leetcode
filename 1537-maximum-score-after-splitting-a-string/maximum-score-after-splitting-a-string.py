class Solution:
    def maxScore(self, s: str) -> int:

        one = s.count("1")
        zero = 0
        best = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                one -= 1
            else: 
                zero += 1
            best = max(best, zero + one)

        return best



        return 3
        """
            Try doing in a one pass
            011101
            all one + all zero = len(s)

            count 0s, as we iterate

            0s, ptr, len(s)

            1s = 

        """
        