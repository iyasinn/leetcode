


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        opens = []
        output = []

        for i, c in enumerate(s):
            if c not in ["(", ")"]:
                output.append(c)
            elif c == "(":
                output.append(c)
                opens.append(len(output) - 1)
            elif c == ")":
                if opens:
                    output.append(c)
                    opens.pop()

        for i in opens:
            output[i] = ""

        return "".join(output)
                
    