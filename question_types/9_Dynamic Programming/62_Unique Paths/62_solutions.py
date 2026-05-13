class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)] #到m-1 n-1的位置一共多少条，不是经过多少点
        for i in range(m):
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        
        return dp[m-1][n-1]