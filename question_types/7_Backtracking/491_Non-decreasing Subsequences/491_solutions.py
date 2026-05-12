class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.path=[]
        def backtracking(pt)->None:
            used=set()
            for i in range(pt,len(nums)):
                if (not self.path or nums[i]>=self.path[-1]) and nums[i] not in used:
                    self.path.append(nums[i])
                    used.add(nums[i])
                    backtracking(i+1)
                    if len(list(self.path))>=2:
                        self.res.append(list(self.path))
                    self.path.pop()
        backtracking(0)
        return self.res