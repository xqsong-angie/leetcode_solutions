class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0 for _ in range(n)] for _ in range(n)]#dp[i][j]代表以i起始以j终止的最大回文子串长度

        for i in range(n):
            dp[i][i]=1
            
        for i in range(n - 1, -1, -1):#从右到左
            for j in range(i + 1, n):#从i到右
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2#左下方的格子
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])#下方或者左方

        return dp[0][n-1]

#20260718 看了一遍，还是不太懂

#20260726拿到题看不出来是dp