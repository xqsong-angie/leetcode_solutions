class Solution:
    def numSquares(self, n: int) -> int:
        #dp[j] is the least number of perfect square numbers sum to n
        dp=[math.inf]*(n+1) #完全背包限制题,同coin change
        dp[0]=0
        for i in range(1,int(sqrt(n))+1):
            for j in range(i**2, n+1):
                dp[j]=min(dp[j],dp[j-i**2]+1) #最小加min
        return dp[n]

#20260717 看了一遍