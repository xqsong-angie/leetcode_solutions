class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.path=[]
        self.res.append([])
        nums.sort()

        def backtracking(pt):
            if pt<len(nums):
                for i in range(pt,len(nums)):
                    if i==pt or (i>pt and nums[i]!=nums[i-1]):
                        self.path.append(nums[i])
                        self.path.extend([])
                        backtracking(i+1)
                        self.res.append(list(self.path))
                        self.path.pop()
        backtracking(0)       
        return self.res