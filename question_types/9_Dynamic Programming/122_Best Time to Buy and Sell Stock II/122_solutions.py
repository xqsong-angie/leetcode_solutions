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

#20260707
#错：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #从来没买过
        #当天不持有(要么昨天卖的，要么昨天之前卖的一直没买)dp[1][i]
        #当天持有（要么昨天刚买入的，要么昨天之前买的一直没卖）dp[2][i]
        n=len(prices)
        dp=[[0]*n for _ in range(3)]
        dp[2][0]=-prices[0]
        for i in range(1,n):
            dp[1][i]=max(dp[2][i-1]+prices[i-1],dp[1][i-1]) #🔥price[i]表示今天的股票价格，应该用price[i]今天我没有股票，要么是昨天及以前卖的，要么是当天卖掉的
            dp[2][i]=max(dp[1][i-1]-prices[i-1],dp[2][i-1])#🔥price[i]表示今天的股票价格，应该用price[i]今天我有股票，要么是昨天及以前买的，要么是当天买入的
        return max(dp[0][n-1],dp[1][n-1],dp[2][n-1])

#对：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #从来没买过
        #当天不持有(要么当天卖的，要么昨天之前卖的一直没买)dp[1][i]
        #当天持有（要么当天刚买入的，要么昨天之前买的一直没卖）dp[2][i]
        n=len(prices)
        dp=[[0]*n for _ in range(3)]
        dp[2][0]=-prices[0]
        for i in range(1,n):
            dp[1][i]=max(dp[2][i-1]+prices[i],dp[1][i-1])
            dp[2][i]=max(dp[1][i-1]-prices[i],dp[2][i-1])
        return max(dp[0][n-1],dp[1][n-1],dp[2][n-1])