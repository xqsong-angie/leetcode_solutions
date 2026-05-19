class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)] #以[i-1][j-1]结尾的s里面有t的个数
        for i in range(m+1):
            dp[i][0]=1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j] #用s[i-1]和不用s[i-1]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]