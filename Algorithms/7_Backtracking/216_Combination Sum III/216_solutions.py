class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res=[]
        self.path=[]
        self.sum=0
        def backtracking(k,n,start_idx,pt)->None:
            if start_idx<k and self.sum<n:
                for i in range(pt,min(n-self.sum+1,10)):
                    self.path.append(i)
                    self.sum+=i
                    backtracking(k,n,start_idx+1,i+1)
                    self.path.pop()
                    self.sum-=i
            elif start_idx==k and self.sum==n:
                self.res.append(list(self.path))
            else:
                return
        backtracking(k,n,0,1)
        return self.res