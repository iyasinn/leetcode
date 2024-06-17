class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(0, floor(math.sqrt(c)) + 1): 
            x = math.sqrt(c - (i * i))
            print(i, x)
            if int(x) == x: 
                return True

        return False




"a^2 + b^2 = c"
"""

sqrt(c) = x
a^2 + b^2 = x^2


we need integers

could try all integers from 1 -> sqrt(x)
And see if sqrt(c - i^2) is an integer


"""


        