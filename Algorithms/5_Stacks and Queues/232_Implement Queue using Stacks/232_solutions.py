#20250922
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


#20260606
class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res=self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res
        

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res=self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res
        

    def empty(self) -> bool:
        return False if self.stack1 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
