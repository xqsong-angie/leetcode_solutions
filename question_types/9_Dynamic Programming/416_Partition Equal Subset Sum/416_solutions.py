class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum=sum(nums)
        if list_sum%2!=0:
            return False
        else:
            target=list_sum//2 #0-1
            dp=[0]*(target+1)
            for i in range(len(nums)): 
                for j in range(target,nums[i]-1,-1):
                        dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])#价值等于重量限制了最大值不可能超过总价值
        return not dp[target]-target
