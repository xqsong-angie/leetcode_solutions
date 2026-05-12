class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.path=[]
        def backtracking()->None: #nums排不排序无所谓
            if len(self.path)<len(nums):
                for i in range(len(nums)): #len(self.path)必须与len(nums)相等
                    if nums[i] not in self.path:
                        self.path.append(nums[i])
                        backtracking()
                        self.path.pop()
            else:
                self.res.append(list(self.path))
        backtracking()
        return self.res