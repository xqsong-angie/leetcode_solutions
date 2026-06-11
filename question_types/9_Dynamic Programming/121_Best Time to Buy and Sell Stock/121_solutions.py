class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0] = 第i天不持有股票时的最大收益
        # dp[i][1] = 第i天持有股票时的最大收益
        dp = [[0, 0] for _ in range(n)]
        
        dp[0][0] = 0              # 第0天不持有：收益为0
        dp[0][1] = -prices[0]     # 第0天持有：花钱买入
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 不持有：昨天就没持有 or 今天卖出
            dp[i][1] = max(dp[i-1][1], -prices[i])               # 持有：昨天就持有 or 今天买入
        
        return dp[n-1][0]  # 最后一天不持有收益最大
    
#20260610
#错误版：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*(n+1) for _ in range(3)] 
        #dp[0][i] 当天不持有（要么是今天卖了，要么是今天以前卖了） 
        #dp[1][i]当天持有(要么是今天买了，要么是今天之前买的，今天还没卖), i是天数
        #dp[2][i]当天卖掉，之后不能选择再买了
        dp[1][1]=-prices[0]
        dp[2][1]=0
        for i in range(1,n+1):
            dp[1][i]=max(dp[0][i-1]-prices[i-1],dp[1][i-1])#当天持有，买了
            dp[2][i]=max(dp[1][i-1]+prices[i-1],dp[2][i-1])#卖掉了
        return max(dp[0][n],dp[2][n])
#正确版
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        # dp[i][0] 表示第 i 天不持有股票，dp[i][1] 表示第 i 天持有股票
        dp = [[0] * 2 for _ in range(n)]
        
        # 初始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 注意这里：是 -prices[i]，而不是 dp[i-1][0] - prices[i]
            # （！！！）因为只能买一次，买入时前面的利润必定为 0
            dp[i][1] = max(dp[i-1][1], -prices[i])
            
        return dp[n-1][0]