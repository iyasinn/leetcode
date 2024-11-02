
# assume a comes before b
def willCollide(a, b):
    aSign = a // abs(a)
    bSign = b // abs(b)
    return aSign == 1 and bSign == -1

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for n in asteroids: 

            destroyed = False

            while not destroyed and stack and willCollide(stack[-1], n):
                destroyed = bool(abs(stack[-1]) >= abs(n))
                if abs(stack[-1]) <= abs(n):
                    stack.pop()
            
            if not destroyed: 
                stack.append(n)


        return stack

        