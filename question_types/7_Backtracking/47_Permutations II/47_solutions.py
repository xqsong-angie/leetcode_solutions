class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        nums.sort()
        self.used = [0] * len(nums) 
        
        def backtracking():
            if len(self.path) == len(nums):#排列问题个数有限制，必须等同于数组自身大小，此时才能收集结果
                self.res.append(list(self.path))
                return

            for i in range(len(nums)):
                # 1. 纵向去重：下标 i 的元素已经在当前 path 里的直接跳过（用过的下标不能再用）
                if self.used[i] == 1:
                    continue
                
                # 2. 横向去重：（用过的值不能再用）
                # 如果当前值等于前一个值，且前一个值 self.used[i-1] == 0
                # 说明前一个相同的数字在“当前层级”已经完全处理完并回溯了
                if i > 0 and nums[i] == nums[i-1] and self.used[i-1] == 0:#例：[1,2(1),2(2)],那在1往下的时候，第二层会有两个分支，分别是2(1),2(2), 会导致结果里有重复，所以要去掉多出来的
                    continue

                self.path.append(nums[i])#没有重复可以再加一个
                self.used[i] = 1
                backtracking()
                
                # 回溯
                self.used[i] = 0#用完弹出了，当前层没用，之后可以用
                self.path.pop()

        backtracking()
        return self.res
    
#20260711 看了一遍