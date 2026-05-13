#20250723
class Solution:
    def rob(self, nums: List[int]) -> int:
        #f[n] is the largest sum n can get
        n=len(nums)
        f=[0]*(n+3)

        #trivial case
        if n==1:
            f[1]=nums[0]
        else:
            f[1]=nums[0]
            f[2]=max(nums[0],nums[1])

            for i in range(3,n+1):
                f[i]=max(f[i-1],f[i-2]+nums[i-1])

        return f[n]

#20250823
class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] is the largest sum can get when there are i houses
        dp=[0]*(len(nums)+1)
        dp[0]=0
        n=len(nums)
        if n==1:
            dp[n]=nums[0]
        elif n==2:
            dp[n]=max(nums)
        elif n>=3:
            dp[1]=nums[0]
            dp[2]=max(nums[0],nums[1])
            for i in range(3,len(nums)+1):
                dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[n]
