class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.path=[]
        self.sum=0
        candidates.sort()
        def backtracking(diff,pt):
            if diff>0:
                for i in range(pt,len(candidates)):
                    if (i==pt) or (i>pt and candidates[i]!=candidates[i-1]):
                        self.path.append(candidates[i])
                        self.sum+=candidates[i]
                        backtracking(target-self.sum,i+1)
                        self.path.pop()
                        self.sum-=candidates[i]
            elif diff==0:
                self.res.append(list(self.path))
            else:
                return       
        backtracking(target-self.sum,0)
        return self.res
            