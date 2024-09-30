class CustomStack:

    def __init__(self, maxSize: int):

        self.stack = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize: 
            return
        self.stack.append([x, 0])
        

    def pop(self) -> int:
        if len(self.stack) == 0: 
            return -1
        
        val, add = self.stack[-1]
        self.stack.pop()

        if len(self.stack) > 0:
            self.stack[-1][1] += add

        return val + add


    def increment(self, k: int, val: int) -> None:
        i = min(k - 1, len(self.stack) - 1)
        
        if i < 0: 
            return

        self.stack[i][1] += val 
        print()


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)