#20260811
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
#错：没有用上述api
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList=nestedList
        self.flattened=[]
        self.idx=None

    def next(self) -> int:
        def dfs(cur):
            if type(cur)==int:
                self.flattened.append(cur)
            else:
                for i in range(len(cur)):
                    dfs(cur[i])
        if not self.flattened:
            cur=self.nestedList
            for i in range(len(cur)):
                dfs(cur[i])
            self.idx=0
        else:
            self.idx+=1
        return self.flattened[self.idx]
        
    def hasNext(self) -> bool:
        if not self.idx or self.idx==len(self.flattened):#🔥这里会直接使 hasNext返回false
            return False
        else:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#对：
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        self.idx = 0
        
        # 在初始化阶段直接做 DFS，把所有数字提取到 flattened 数组中
        def dfs(nList):
            for item in nList:
                if item.isInteger():
                    # 必须使用提供的 getInteger() 方法来获取数字
                    self.flattened.append(item.getInteger())
                else:
                    # 必须使用提供的 getList() 方法来获取下一层列表
                    dfs(item.getList())
        
        # 启动 DFS
        dfs(nestedList)#🔥__init__里面的代码可以直接执行

    def next(self) -> int:
        # 获取当前指向的数字，并将索引 +1
        res = self.flattened[self.idx]
        self.idx += 1
        return res
        
    def hasNext(self) -> bool:
        # 只要当前索引没有走到数组末尾，就说明还有元素
        return self.idx < len(self.flattened)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())