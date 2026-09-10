class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dp[j]: the number of combinations adds up to j(with order) 这道题求排列数，不是组合数，又不一样了
        dp=[0]*(target+1)
        dp[0]=1
        for j in range(target+1):#排列数，背包在外，因为分别尝试了nums终端每一个数为最后一个元素，而组合的情况必须物品在外，因为确定了物品的顺序，否则会有重复
            for i in range(len(nums)):
                if j>=nums[i]:
                    dp[j]+=dp[j-nums[i]]
        return dp[target]
    
#20260717 看了一遍

#0-1背包组合：物品外，容量内倒序
#完全背包组合：物品外，容量内正序
#0-1背包排列：容量外，物品内标记visited
#完全背包排列：容量外，物品内正序