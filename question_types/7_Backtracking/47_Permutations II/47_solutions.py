class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        nums.sort()
        self.used = [0] * len(nums) 
        
        def backtracking():
            if len(self.path) == len(nums):
                self.res.append(list(self.path))
                return

            for i in range(len(nums)):
                # 1. 纵向去重：下标 i 的元素已经在当前 path 里的直接跳过
                if self.used[i] == 1:
                    continue
                
                # 2. 横向去重：
                # 如果当前值等于前一个值，且前一个值 self.used[i-1] == 0
                # 说明前一个相同的数字在“当前层级”已经完全处理完并回溯了
                if i > 0 and nums[i] == nums[i-1] and self.used[i-1] == 0:
                    continue

                self.path.append(nums[i])
                self.used[i] = 1
                backtracking()
                
                # 回溯
                self.used[i] = 0
                self.path.pop()

        backtracking()
        return self.res