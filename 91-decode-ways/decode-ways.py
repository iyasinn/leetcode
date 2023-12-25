"""

Decode a string by considering each letter as two letters or one letter? 
If we consider it as two letters, then we can consider a smaller subproblem 
Some numbers are invalid
They need to be between 1 and 27

Lets try a recursive approach 
"""


def valid(s):
    if len(s) == 2 and s[0] == '0': 
        return False
    
    n = int(s)
    return n >= 1 and n <= 26


@cache
def rec(s, i):
    if i < 0: 
        return 1
    if i == 0: 
        return int(valid(s[0]))

    one_digit = valid(s[i])
    two_digit = valid(s[i-1:i+1])

    ways = 0 

    if one_digit: 
        ways += rec(s, i - 1)
    if two_digit: 
        ways += rec(s, i - 2)

    print(ways)
    return ways


class Solution:
    def numDecodings(self, s: str) -> int:
        return rec(s, len(s) - 1)
        


