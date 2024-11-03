class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        stack = []

        for n in path: 
            if n in " .":
                continue
            elif n == ".." and stack:
                stack.pop()
            elif n != "..":
                stack.append(n)

        return "/" + "/".join(stack)



        