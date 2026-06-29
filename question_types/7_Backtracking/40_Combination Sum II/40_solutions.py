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

#20260628
#错：
def  subsetSums(nums, target):
    nums.sort()
    res=[]
    path=[]
    n=len(nums)
    if sum(nums)<target:
        return []
    def backtracking(pt, nums, target,path):
        if pt<n:
            for i in range(pt,n):
                if sum(path)<target:
                    path.append(nums[i])
                    backtracking(pt+1,nums,target,path) #i+1
                    path.pop()
                elif sum(path)==target:
                    res.append(list(path))
    backtracking(0,nums,target,path)
    return res

#对：
def  subsetSums(nums, target):
    nums.sort()
    res=[]
    path=[]
    n=len(nums)
    if sum(nums)<target:
        return []
    def backtracking(pt, cur_sum):
        if cur_sum==target:
            res.append(list(path))
        if cur_sum>target:
            return
        for i in range(pt,n):
            path.append(nums[i])
            backtracking(i+1,cur_sum+nums[i])
            path.pop()

    backtracking(0,0)
    return res
            