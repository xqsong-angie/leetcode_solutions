class MyStack:

    def __init__(self):
        self.inqueue=[]
        self.outqueue=[]

    def push(self, x: int) -> None:
        self.inqueue.append(x)

    def pop(self) -> int:
        n=len(self.inqueue)
        if n==0:
           return None 
        for _ in range(n-1):
            top=self.inqueue.pop(0)
            self.outqueue.append(top)
        top=self.inqueue.pop(0)
        self.inqueue, self.outqueue = self.outqueue, self.inqueue
        return top
        

    def top(self) -> int:
        while self.inqueue:
            top=self.inqueue.pop(0)
            self.outqueue.append(top)
        self.inqueue, self.outqueue = self.outqueue, self.inqueue
        return top

    def empty(self) -> bool:
        if not self.inqueue and not self.outqueue:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()