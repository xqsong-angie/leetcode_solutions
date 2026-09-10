from collections import defaultdict
class Solution:
    def __init__ (self):
        self.father=[]

    def init(self,n):
        self.father=[i for i in range(n+1)]

    def find(self,u):
        if u==self.father[u]:
            return u
        else:
            self.father[u]=self.find(self.father[u])
            return self.father[u]

    def isSame(self,u,v):
        u=self.find(u)
        v=self.find(v)
        if u==v:
            return True
        else:
            return False

    def join(self,u,v):
        u=self.find(u)
        v=self.find(v)
        if u==v:
            return
        else:
            self.father[u]=v

    #🔥“原本是一棵合法的 N 个节点、N-1 条边的有向树，后来有人多加了一条边，变成了 N 条边。”
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:#比684难在有向图
        #1.找到入度为2的点（🔥有向树的定义，每个节点最多有一个父亲，即入度最多一条，有向树指父亲指向孩子）
        n=len(edges)
        self.init(n)
        indegree=defaultdict(lambda: 0)
        for s,t in edges:
            #判断入度为2
            indegree[t]+=1

        #2.记录入度为2对应的那两条候选边，决定删哪一条
        cand1=cand2=None
        for s,t in edges:
            if indegree[t]==2:
                if cand1 is None:
                    cand1=[s,t] #记录先出现的那一条
                else:
                    cand2=[s,t] #记录后出现的那一条
        #3.1 有入度为2的点
        if cand2:
            #优先选择跳过cand2，建并查集（假设删掉的是这条边，看剩下的合不合法），看是否有环
            self.init(n)
            for s,t in edges:
                if[s,t]==cand2:#跳过cand2
                    continue
                if self.isSame(s,t):#说明有环，那么cand2不是要删的，应该删环内的
                    return cand1
                self.join(s,t)
            return cand2 #说明无环，删cand2
        #3.2无入度为2的点，直接删环内一条
        else:
            self.init(n)
            for s,t in edges:
                if self.isSame(s,t):
                    return [s,t]
                else:
                    self.join(s,t)
            

#20260723 看了一遍