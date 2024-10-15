# Need all the 1s to the right
# So this is the distance to the end - 1

"""

10

1

"""

class Solution:
    def minimumSteps(self, s: str) -> int:

        black = 0
        steps = 0

        for c in s:
            if c == "0":
                steps += black
            else:
                black += 1
        return steps


        # steps = 0 
        # end = len(s) - 1

        # for i in range(len(s)):
        #     if s[i] == "0":
        #         continue
        #     steps += (end - i)
        #     end -= 1

        # return steps
        