class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n)
        dp[0]=1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=1
        return max(dp)