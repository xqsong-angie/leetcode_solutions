class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.path=[]
        self.sum=0
        def backtracking(diff,start_idx):
            if diff>0:
                for i in range(start_idx,len(candidates)):
                    self.path.append(candidates[i])
                    self.sum+=candidates[i]
                    backtracking(target-self.sum,i)
                    self.path.pop()
                    self.sum-=candidates[i]
            elif diff==0:
                self.res.append(list(self.path))
            else:
                return
        backtracking(target-self.sum,0)
        return self.res