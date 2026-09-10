class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.path=[]
        self.res.append([])#先放入空集
        nums.sort()

        def backtracking(pt):
            if pt<len(nums):
                for i in range(pt,len(nums)):
                    if i==pt or (i>pt and nums[i]!=nums[i-1]):
                        self.path.append(nums[i])
                        backtracking(i+1)
                        self.res.append(list(self.path))#每层都可以收集一回结果，子集问题没有个数限制
                        self.path.pop()
        backtracking(0)       
        return self.res
    
#20260711 看了一遍
