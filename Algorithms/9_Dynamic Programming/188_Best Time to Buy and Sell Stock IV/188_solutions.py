class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[ [0 for _ in range(2*k+1)] for _ in range(n+1)]#dp[i][j]代表第i天进行第j次交易
        if n==1:
            return 0
        else:
            #initialization
            for i in range(1,2*k+1):
                if i%2!=0:#对于第一天进行第i次交易，交易为奇数则买
                    dp[1][i]=-prices[0]
            #updating
            for i in range(2,n+1):
                for j in range(1,2*k+1):
                    if j%2!=0:#k为奇数，多出来那次是买的
                        dp[i][j]=max(dp[i][j-1]-prices[i-1],dp[i-1][j])
                    else:#k为偶数，刚好出掉手上的
                        dp[i][j]=max(dp[i][j-1]+prices[i-1],dp[i-1][j])
            return dp[n][2*k]
        
#20260717 看了一遍