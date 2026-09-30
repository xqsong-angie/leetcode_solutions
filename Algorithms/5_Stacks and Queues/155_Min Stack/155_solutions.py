#20260929
class MinStack:

    def __init__(self):
        self.low=[]#递增栈
        self.high=[]#递减栈
        self.low_size=0
        self.high_size=0

    def push(self, value: int) -> None:
        if value>self.low[-1]:
            self.high.append()
        self.low.append(value) #🔥这里想用两个单调栈，但是单调栈弹出再放回去是O(n)的

    def pop(self) -> None:
        return self.low.pop()

    def top(self) -> int:
        return self.low[-1]

    def getMin(self) -> int:
        return self.high[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#答案
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # 存每个状态下的最小值

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果辅助栈为空，直接压入；否则压入当前值与栈顶最小值的较小者
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()#🔥代表在len(stack)高度上，全局最小值快照（这个真的不好想）

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]