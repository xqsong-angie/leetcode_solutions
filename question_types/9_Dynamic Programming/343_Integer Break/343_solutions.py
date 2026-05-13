class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+3)
        dp[2]=1
        for i in range(3,n+1):
            for j in range(1,i//2+1):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])

        return dp[n]

#从前向后推，每一个分割点dp[i+1]相当于是从上一个dp[i]走了一步（类似爬楼梯）得来。注意此方法不包含直接两步的，相当于之前是一步登天没走dp，然后差临门一脚的单独算。

