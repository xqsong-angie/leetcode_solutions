class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        # State definitions:
        # hold    : max profit when holding a stock
        # cooldown: max profit on the day after selling (cooldown day)
        # free    : max profit when not holding, and free to buy

        dp = [[0] * 3 for _ in range(n + 1)]
        #          [hold, cooldown, free]
        dp[1][0] = -prices[0]  # hold
        dp[1][1] = 0           # cooldown
        dp[1][2] = 0           # free

        for i in range(2, n + 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i-1])  # keep holding | buy (only from free)
            dp[i][1] = dp[i-1][0] + prices[i-1]                    # sell today → enter cooldown
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])                 # stay free  | cooldown expired

        return max(dp[n][1], dp[n][2])
