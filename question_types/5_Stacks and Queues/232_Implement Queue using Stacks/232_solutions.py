class MyQueue:

    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        while self.instack:
            self.outstack.append(self.instack.pop())
        top=self.outstack.pop()
        while self.outstack:
            self.instack.append(self.outstack.pop())
        return top

    def peek(self) -> int:
        while self.instack:
            self.outstack.append(self.instack.pop())
        top=self.outstack[-1]
        while self.outstack:
            self.instack.append(self.outstack.pop())
        return top

    def empty(self) -> bool:
        if not self.instack:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()