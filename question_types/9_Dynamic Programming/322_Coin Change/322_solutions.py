class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[j] stands for the min number of coins to make up j
        dp=[math.inf]*(amount+1)
        dp[0]=0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]=min(dp[j],dp[j-coins[i]]+1)#完全背包组合有限制（最少硬币数）题
        if dp[amount]==inf and amount!=0:#说明没有更新过
            return -1
        else:
            return dp[amount]
        
#20260717 看了一遍