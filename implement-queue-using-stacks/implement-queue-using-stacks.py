class MyQueue:

    def transfer(self):
        if (len(self.head) > 0):
            return

        while (len(self.tail) > 0):
            self.head.append(self.tail.pop())     

    def __init__(self):
        self.tail = []
        self.head = []        

    def push(self, x: int) -> None:
        self.tail.append(x)

    def pop(self) -> int:
        self.transfer()    
        return self.head.pop()
        

    def peek(self) -> int:
        self.transfer()
        return self.head[-1]
        

    def empty(self) -> bool:
        return (len(self.head) + len(self.tail)) == 0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()