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