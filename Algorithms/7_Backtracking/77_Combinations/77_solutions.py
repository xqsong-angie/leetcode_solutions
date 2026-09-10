class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        self.path=[]
        def backtracking(n,k,start_idx,pt)->None:
            if start_idx<k:#已经选了几个
                for i in range(pt,n+1): #pt代表从哪个数开始选
                    self.path.append(i)
                    backtracking(n,k,start_idx+1,i+1)#进入下一层,从i右侧的数开始
                    self.path.pop()#分别尝试当前层可尝试的所有数
            else:#已经选了k个了
                self.res.append(list(self.path))#放一个结果
        backtracking(n,k,0,1)
        return self.res
    
#20260711 看了一遍
