class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for _ in range(5)] for _ in range(n + 1)]
        if n==1:
            return 0
        else:
            #dp[1][0]从来没有任何操作过
            dp[1][1]=-prices[0] #第一次买入
            dp[1][2]=0 #第一次卖出
            dp[1][3]=-prices[0] #第二次买入
            dp[1][4]=0 #第二次卖出
            for i in range(2,n+1): #第i天的情况
                dp[i][1]=max(dp[i][0]-prices[i-1],dp[i-1][1]) #第一次持有，手里的没卖
                dp[i][2]=max(dp[i][1]+prices[i-1],dp[i-1][2]) #第一次不持有，不知道哪天卖出去的
                dp[i][3]=max(dp[i][2]-prices[i-1],dp[i-1][3]) #第二次持有，手里的没卖
                dp[i][4]=max(dp[i][3]+prices[i-1],dp[i-1][4]) #第二次不持有，不知道哪天卖出去的

            return dp[n][4]