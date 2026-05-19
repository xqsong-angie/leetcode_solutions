class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*(n+1) for _ in range(2)]
        #第一天不持有
        dp[0][1]=0
        #第一天持有
        dp[1][1]=-prices[0]
        for i in range(2,n+1):
            #今天不持有:max(昨天不持有，昨天持有今天卖掉)
            dp[0][i]=max(dp[0][i-1],dp[1][i-1]+prices[i-1])
            #今天持有:max(昨天持有今天不卖，昨天不持有今天买)
            dp[1][i]=max(dp[1][i-1],dp[0][i-1]-prices[i-1])
        
        return max(dp[1][n],dp[0][n])
