class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[j] as the number of combinations when weight equals to j
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]+=dp[j-coins[i]]
        return dp[amount]