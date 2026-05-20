class Solution:
    #并查集
    def __init__ (self):
        self.father=[]

    def init(self,n):
        self.father=[i for i in range (n+1)]
        #初始化，一个节点占一个集合

    def find(self, u):#用来找u的根节点
        if u==self.father[u]:
            return u
        else:
            self.father[u]=self.find(self.father[u]) #路径压缩，当前节点到根节点只有一步
            return self.father[u]

    def isSame(self,u,v): # if u, v are in the same set（如何判断两者是否属于一个集合？即是否有共同根节点）
        u=self.find(u)
        v=self.find(v)
        if u==v:
            return True
        else:
            return False
    def join(self, u, v):
        u=self.find(u) #看看u的根
        v=self.find(v)#看看v的根
        if u==v:#如果u与v在同一集合，无需join
            return 
        else:#如果不在，要把两者并根
            self.father[v]=u

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        self.init(n)
        for s,t in edges:
            if self.isSame(s,t): #如果检测到两个点已经在同一个connected components(set)里面，多出来的这条边就是多的
                return [s,t]
            else: #否则连接两个点
                self.join(s,t)
    

