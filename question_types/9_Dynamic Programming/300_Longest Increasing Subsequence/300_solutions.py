class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n#至少有一个

        for i in range(n):#上线位置
            for j in range(i):
                if nums[i]>nums[j]:#严格递增，相等不行
                    dp[i]=max(dp[i],dp[j]+1)
                
        return max(dp)
    
#20260717 看了一遍