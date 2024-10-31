


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        opens = []
        closed = set()

        for i, c in enumerate(s):
            if c not in ["(", ")"]:
                continue
            if c == "(":
                opens.append(i)
            elif c == ")":
                if not opens:
                    closed.add(i)
                else:
                    opens.pop()
        opens = set(opens)
        output = []

        for i, c in enumerate(s):
            if i in opens or i in closed: 
                continue
            output.append(c)

        return "".join(output)
                
        