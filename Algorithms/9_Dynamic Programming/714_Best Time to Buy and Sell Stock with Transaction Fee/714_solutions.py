class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[ [0]*3 for _ in range(n+1)]
        if n==1:
            return 0
        else:
            dp[1][1]=-prices[0]#持有
            dp[1][2]=-fee#不持有
            for i in range(2,n+1):
                dp[i][1]=max(dp[i-1][2]-prices[i-1],dp[i-1][1],dp[i-1][0]-prices[i-1])#持有
                dp[i][2]=max(dp[i-1][1]+prices[i-1]-fee,dp[i-1][2],dp[i-1][0])#不持有

        return max(dp[n][1],dp[n][2])