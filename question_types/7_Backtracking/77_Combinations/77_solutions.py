class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res=[]
        self.path=[]
        def backtracking(n,k,start_idx,pt)->None:
            if start_idx<k:
                for i in range(pt,n+1):
                    self.path.append(i)
                    backtracking(n,k,start_idx+1,i+1)
                    self.path.pop()
            else:
                self.res.append(list(self.path))
        backtracking(n,k,0,1)
        return self.res