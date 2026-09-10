#20250922
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

#20260606
class MyStack:

    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        res=self.queue1.pop(0)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))    
        return res

    def top(self) -> int:
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        res=self.queue1.pop(0)
        self.queue2.append(res)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return res

    def empty(self) -> bool:
        return False if self.queue1 else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()