class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[ [0 for _ in range(2*k+1)] for _ in range(n+1)]
        if n==1:
            return 0
        else:
            #initialization
            for i in range(1,2*k+1):
                if i%2!=0:
                    dp[1][i]=-prices[0]
            #updating
            for i in range(2,n+1):
                for j in range(1,2*k+1):
                    if j%2!=0:
                        dp[i][j]=max(dp[i][j-1]-prices[i-1],dp[i-1][j])
                    else:
                        dp[i][j]=max(dp[i][j-1]+prices[i-1],dp[i-1][j])
            return dp[n][2*k]