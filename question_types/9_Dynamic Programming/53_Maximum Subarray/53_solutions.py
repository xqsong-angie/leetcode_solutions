class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for _ in range(n+1)]
        if n==1:
            return sum(nums)
        else:
            for i in range(1,n+1):
                dp[i]=max(dp[i]+nums[i-1],dp[i-1]+nums[i-1])
                
            return max(dp[1:n+1])
