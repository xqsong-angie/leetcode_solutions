class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum=sum(nums)
        if list_sum%2!=0:
            return False
        else:
            target=list_sum//2 #dp经典题目之0-1背包，如果能达到target,说明另外一半也能达到target
            dp=[0]*(target+1) 
            for i in range(len(nums)): #物品
                for j in range(target,nums[i]-1,-1):#背包大小，物品和价值一致
                        dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])#价值等于重量限制了最大值不可能超过总价值
        return not dp[target]-target

#20260712 看了一遍