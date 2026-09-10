class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[j] as the number of combinations when weight equals to j 完全背包
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)):#物品
            for j in range(coins[i],amount+1):#容量，每拿一个物品，都遍历物品及以上的位置看看能不能多放一个，不能倒序，倒序是0-1背包
                dp[j]+=dp[j-coins[i]]
        return dp[amount]
    
#20260717 看了一遍