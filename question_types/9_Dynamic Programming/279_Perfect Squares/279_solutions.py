class Solution:
    def numSquares(self, n: int) -> int:
        #dp[j] is the least number of perfect square numbers sum to n
        dp=[math.inf]*(n+1)
        dp[0]=0
        for i in range(1,int(sqrt(n))+1):
            for j in range(i**2, n+1):
                dp[j]=min(dp[j],dp[j-i**2]+1)
        return dp[n]
