# Need all the 1s to the right
# So this is the distance to the end - 1

"""


"""

class Solution:
    def minimumSteps(self, s: str) -> int:

        steps = 0 
        end = len(s) - 1


        for i in range(len(s)):
            if s[i] == "0":
                continue

            steps += (end - i)
            end -= 1

        return steps
        