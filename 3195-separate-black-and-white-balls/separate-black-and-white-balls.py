# Need all the 1s to the right
# So this is the distance to the end - 1

"""


"""

class Solution:
    def minimumSteps(self, s: str) -> int:

        steps = 0 
        blacks = 0

        for i in range(len(s)):
            if s[i] == "0":
                continue

            desEnd = len(s) - 1 - blacks

            steps += (desEnd - i)

            blacks += 1

        return steps
        