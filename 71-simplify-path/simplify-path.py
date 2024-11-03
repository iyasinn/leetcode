class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = []

        for n in path: 
            if n == "":
                continue
            if n == ".":
                continue
            if n == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(n)

        print(stack)
        return "/" + "/".join(stack)



        