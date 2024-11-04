

"""

x^4

x * x * x * x

x^(4/2 + 4/2)

x^(4/2) * x^(4/2)

n is even:
x^n = x^(n/2) * x^(n/2)



n is odd
x^n = x * x^(n/2) * x^(n/2)



"""



class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            n = n * -1
            x = 1 / x

        def dfs(x, n):
            if n == 0: 
                return 1
            curr = self.myPow(x * x, n // 2)
            return curr * (1 if n % 2 == 0 else x)

        return dfs(x, n)
            