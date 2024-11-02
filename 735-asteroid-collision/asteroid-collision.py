
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for n in asteroids: 
            destroyed = False
            while not destroyed and stack and stack[-1] > 0 and n < 0:
                destroyed = bool(abs(stack[-1]) >= abs(n))
                if abs(stack[-1]) <= abs(n):
                    stack.pop()
            if not destroyed: 
                stack.append(n)
        return stack

        